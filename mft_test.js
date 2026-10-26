"use strict";
/* Shape test for WebGame/js/telemetry.js: stubs the game globals, replays a scripted session,
   and checks every new event comes out with the schema fields. */
const fs = require("fs"), vm = require("vm");

// ---- stubs of the game globals telemetry.js reads ----
global.window = global;
global.SIM = false;
global.QS = { has: () => false };
const listeners = {};
global.on = (ev, fn) => { (listeners[ev] = listeners[ev] || []).push(fn); };
global.emit = (ev, d) => { for (const fn of listeners[ev] || []) fn(d); };
global.W = 360; global.S = 72; global.JL = -2.4; global.JR = 2.4; global.FLOOR = 0.73; global.DANGER = 6.65;
global.X = u => 180 + u * 72;
global.gU = { x: px => (px - 180) / 72, y: py => 0.73 + (600 - 22 - py) / 72 };
global.pieces = new Set();
global.scene = { def: { n: 5, cls: "M", drops: 10 } };
global.st = { time: 0, drops: 0, budget: 10, breach: 0, over: null, danger: 6.65, helps: 0, boosters: 0 };
global.ui = { playing: true, mode: "level" };
global.tick = function (dt) { global.st.time += dt; };
global.doHelp = function (kind) { return "helped:" + kind; };
global.spendBooster = function (id) { return "boost:" + id; };
global.__sim = {
  attempt(def, iq) { emit("build", def); st.drops++; emit("drop", { tier: 1, x: 180 }); return { over: "win" }; },
  replay() { return { over: "win" }; }
};

vm.runInThisContext(fs.readFileSync("D:/Auto/Mossfolk200/WebGame/js/telemetry.js", "utf8"), { filename: "telemetry.js" });

const evs = () => window.MFT.events;
const last = ev => { const l = evs().filter(e => e.event === ev && e.actor === "human"); return l[l.length - 1]; };
const fails = [];
function need(ev, fields, pred) {
  const e = last(ev);
  if (!e) { fails.push(ev + ": never logged"); return; }
  for (const f of fields) if (!(f in e)) fails.push(ev + ": missing field " + f);
  if (pred && !pred(e)) fails.push(ev + ": bad values " + JSON.stringify(e));
}

// ---- scripted session (human) ----
emit("build", scene.def);                                      // attempt_start
st.time = 1.2; st.drops = 1;
pieces.add({ isStatic: false, position: { x: 180, y: 500 }, circleRadius: 20 });
emit("drop", { tier: 1, x: 180 });                             // extended drop (x = centre -> .5)
st.time = 1.5; emit("merge", { tier: 2, chain: 1 });
st.time = 1.9; emit("merge", { tier: 3, chain: 2 });           // two merges inside the cascade window
st.time = 6.0; st.drops = 2; emit("drop", { tier: 0, x: 60 }); // flushes cascade + idle_gap (4.1 s)
// near miss: breach grows then clears
st.breach = .5; tick(.1); st.breach = .2; tick(.1); st.breach = 0; tick(.1);
// fail -> retry -> win
st.over = "full"; tick(.01);                                   // level_fail streak 1
emit("build", scene.def);                                      // retry logged (same level)
st.over = null; st.time = 0;
st.over = "win"; tick(.01);                                    // level_complete
// assist (wrapped doHelp / spendBooster)
st.over = null;
if (doHelp("seeds") !== "helped:seeds") fails.push("doHelp wrap broke the return value");
if (spendBooster("shake") !== "boost:shake") fails.push("spendBooster wrap broke the return value");
// session rhythm: 61 s of play in one tick
tick(61);
// bot tagging
const botBefore = evs().length;
__sim.attempt(scene.def, "average");
const botEvs = evs().slice(botBefore);
if (!botEvs.length || !botEvs.every(e => e.actor === "bot:average")) fails.push("bot events not tagged bot:average: " + JSON.stringify(botEvs.map(e => [e.event, e.actor])));
if (window.MFT.actor !== "human") fails.push("actor did not reset to human after attempt");

// ---- checks ----
need("attempt_start", ["level", "cls", "budget", "actor"], e => e.level === 5 && e.actor === "human");
need("drop", ["x", "rot", "piece_tier", "think_ms", "drag_len", "cancels", "jar_fill_pct", "danger_height", "rt_ms", "level_ms", "actor"],
  e => e.x >= 0 && e.x <= 1 && e.piece_tier === 0);
need("merge_tier", ["tier", "chain"]);
need("cascade", ["depth", "peak_tier", "tiers"], e => e.depth === 2 && e.peak_tier === 3 && e.tiers.length === 2);
need("idle_gap", ["before", "ms", "jar_fill_pct", "danger_height"], e => e.ms >= 3000);
need("near_miss", ["breach_ms", "jar_fill_pct", "danger_height"], e => e.breach_ms >= 350);
need("level_fail", ["reason", "drops", "budget", "streak"], e => e.reason === "full" && e.streak === 1);
need("retry", ["level_id", "latency_ms", "streak"], e => e.level_id === 5 && e.streak === 1);
need("level_complete", ["drops", "budget", "helps", "boosters"]);
need("assist_context", ["kind", "source", "jar_fill_pct", "danger_height", "drops", "budget", "streak"], e => e.source === "booster");
need("session_rhythm", ["minute", "drops_per_min", "merges_per_min"]);
const d1 = evs().filter(e => e.event === "drop")[0];
if (d1.x !== 0.5) fails.push("drop x not relative to jar width: " + d1.x);

if (fails.length) { console.log("FAIL\n" + fails.join("\n")); process.exit(1); }
console.log("OK — " + evs().length + " events. Samples:");
for (const ev of ["drop", "cascade", "idle_gap", "near_miss", "retry", "assist_context", "session_rhythm"]) console.log(JSON.stringify(last(ev)));
console.log("bot sample: " + JSON.stringify(botEvs.find(e => e.event === "drop")));
process.exit(0);
