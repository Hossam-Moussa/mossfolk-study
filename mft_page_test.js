"use strict";
/* Real-page smoke test: serves WebGame, opens the real game headless (telemetry on), plays two drops on
   level 1, and prints the [mf-ev] lines the page logged. Also opens a ?sim=1 page and asserts telemetry is OFF there. */
const fs = require("fs"), os = require("os"), path = require("path"), http = require("http");
const { spawn } = require("child_process");
const ROOT = "D:/Auto/Mossfolk200/WebGame";
const sleep = ms => new Promise(r => setTimeout(r, ms));
const CHROME = ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"].find(p => fs.existsSync(p));

function serve() {
  const MIME = { ".html": "text/html", ".js": "application/javascript", ".css": "text/css", ".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg", ".ttf": "font/ttf", ".json": "application/json" };
  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split("?")[0]); if (p.endsWith("/")) p += "index.html";
    const f = path.resolve(path.join(ROOT, p));
    fs.readFile(f, (e, b) => { if (e) { res.writeHead(404).end(); return; } res.writeHead(200, { "Content-Type": MIME[path.extname(f)] || "application/octet-stream", "Cache-Control": "no-store" }); res.end(b); });
  });
  return new Promise(r => srv.listen(0, "127.0.0.1", () => r(srv)));
}
class CDP {
  constructor(url) {
    this.id = 0; this.pending = new Map(); this.console = [];
    this.ws = new WebSocket(url);
    this.ready = new Promise((res, rej) => { this.ws.onopen = res; this.ws.onerror = () => rej(new Error("cdp socket error")); });
    this.ws.onmessage = ev => {
      const m = JSON.parse(ev.data);
      if (m.method === "Runtime.consoleAPICalled") { const t = (m.params.args || []).map(a => a.value).join(" "); this.console.push(t); }
      if (m.id && this.pending.has(m.id)) { const p = this.pending.get(m.id); this.pending.delete(m.id); m.error ? p.rej(new Error(m.error.message)) : p.res(m.result); }
    };
  }
  send(method, params = {}) { const id = ++this.id; this.ws.send(JSON.stringify({ id, method, params })); return new Promise((res, rej) => { this.pending.set(id, { res, rej }); setTimeout(() => { if (this.pending.delete(id)) rej(new Error("timeout " + method)); }, 60000); }); }
  async eval(expr) { const r = await this.send("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception ? r.exceptionDetails.exception.description : r.exceptionDetails.text); return r.result.value; }
}
async function page(port, url) {
  let t;
  for (let i = 0; i < 40 && !(t && t.webSocketDebuggerUrl); i++) { try { t = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: "PUT" })).json(); } catch (e) { await sleep(300); } }
  const cdp = new CDP(t.webSocketDebuggerUrl); await cdp.ready;
  await cdp.send("Runtime.enable"); await cdp.send("Page.enable");
  await cdp.send("Page.navigate", { url });
  for (let i = 0; i < 120; i++) { await sleep(250); try { if (await cdp.eval('typeof window.MFT === "object" && typeof Matter === "object"')) break; } catch (e) {} }
  return cdp;
}
(async () => {
  const srv = await serve(), port = srv.address().port;
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), "mfttest-"));
  const DBG = 9333 + Math.floor(Math.random() * 200);
  const ch = spawn(CHROME, ["--headless=new", "--disable-gpu", "--mute-audio", "--no-first-run", "--window-size=375,812",
    `--user-data-dir=${profile}`, `--remote-debugging-port=${DBG}`, "about:blank"], { stdio: "ignore" });
  try {
    for (let i = 0; i < 60; i++) { try { await (await fetch(`http://127.0.0.1:${DBG}/json/list`)).json(); break; } catch (e) { await sleep(300); } }
    // 1) the real game page, telemetry on
    const p1 = await page(DBG, `http://127.0.0.1:${port}/index.html?level=1&play`);
    console.log("game page MFT.enabled =", await p1.eval("window.MFT.enabled"));
    // close the start card (Play) and drop twice at the same spot -> a merge and its telemetry
    await p1.eval(`(() => { const b = document.querySelector("#cardBox [data-primary]"); if (b) b.click(); return !!b; })()`);
    await sleep(700);
    console.log("playing =", await p1.eval("ui.playing"), "level =", await p1.eval("scene.def.n"));
    await p1.eval("act.drop(X(-1.0))"); await sleep(900);
    await p1.eval("act.drop(X(-1.0))"); await sleep(1600);
    await p1.eval("act.drop(X(1.0))"); await sleep(5200);   // > 3 s silence, the 4th drop should log idle_gap
    await p1.eval("act.drop(X(1.0))"); await sleep(900);
    const evs = await p1.eval("window.MFT.events.map(e => e.event)");
    console.log("page events:", JSON.stringify(evs));
    for (const line of p1.console.filter(l => l.startsWith("[mf-ev]"))) console.log(line);
    const errs = p1.console.filter(l => /error|Error/.test(l) && !l.startsWith("[mf-ev]"));
    console.log("page errors:", errs.length ? JSON.stringify(errs) : "none");
    // 2) a plain ?sim page: telemetry must be OFF and __sim intact
    const p2 = await page(DBG, `http://127.0.0.1:${port}/index.html?sim=1`);
    console.log("sim page MFT.enabled =", await p2.eval("window.MFT.enabled"),
      "| __sim.attempt native =", await p2.eval('String(__sim.attempt).includes("measuring")'));
    const r = await p2.eval(`(() => { const o = __sim.attempt(__sim.def(1), "average", 7, 20, false); return { over: o.over, drops: o.drops }; })()`);
    console.log("sim attempt on level 1:", JSON.stringify(r), "| events logged in sim page =", await p2.eval("window.MFT.events ? window.MFT.events.length : 0"));
    // 3) a sim page with &mft=1: bot events tagged
    const p3 = await page(DBG, `http://127.0.0.1:${port}/index.html?sim=1&mft=1`);
    await p3.eval(`__sim.attempt(__sim.def(1), "average", 7, 20, false)`);
    console.log("mft sim actors:", JSON.stringify(await p3.eval("Array.from(new Set(window.MFT.events.map(e => e.actor)))")),
      "events:", await p3.eval("window.MFT.events.length"));
    console.log("mft sim sample:", JSON.stringify(await p3.eval(`window.MFT.events.find(e => e.event === "drop")`)));
  } finally { try { ch.kill(); } catch (e) {} srv.close(); setTimeout(() => process.exit(0), 500); }
})().catch(e => { console.error("FAILED:", e.message); process.exit(1); });
