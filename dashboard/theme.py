"""WebIntelX AI visual layer: restrained dark SOC theme + small HTML components.
Pure presentation. Every dynamic string goes through html.escape; severity is always shown as TEXT + colour (never colour alone).
Numbers shown come from the caller (measured data) - nothing here invents figures."""
from __future__ import annotations

from html import escape as _e

CSS = """
<style>
:root{--bg:#0b0e14;--s1:#121722;--s2:#171d2b;--bd:#242c3d;--tx:#e6e9ef;--mut:#8b94a7;--ai:#7c8cff;--ok:#3fb27f;--warn:#e0a63a;--hi:#e8743b;--crit:#e5484d}
.block-container{padding-top:1.4rem;max-width:1400px}
[data-testid="stSidebar"]{background:var(--s1);border-right:1px solid var(--bd)}
[data-testid="stMetric"]{background:var(--s1);border:1px solid var(--bd);border-radius:12px;padding:14px 16px}
[data-testid="stMetricLabel"]{color:var(--mut)}
[data-testid="stMetricValue"]{font-weight:650}
div[data-testid="stVerticalBlockBorderWrapper"]{background:var(--s1);border-color:var(--bd)!important;border-radius:12px}
button[kind="secondary"],button[kind="primary"]{border-radius:8px}
.wx-brand{font-weight:700;font-size:1.15rem;letter-spacing:.2px}.wx-sub{color:var(--mut);font-size:.8rem;margin-top:-2px}
.wx-health{font-size:.78rem;color:var(--mut);margin-top:10px}.wx-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--ok);margin-right:6px}
.wx-h1{font-size:1.7rem;font-weight:700;margin:0}.wx-tag{color:var(--mut);margin:2px 0 14px}
.wx-pill{display:inline-block;padding:2px 9px;border-radius:999px;font-size:.72rem;font-weight:650;letter-spacing:.4px;border:1px solid}
.sev-CRITICAL{color:#ff8a8d;border-color:var(--crit);background:#e5484d1a}.sev-HIGH{color:#ff9a63;border-color:var(--hi);background:#e8743b1a}
.sev-MEDIUM{color:#f0c060;border-color:var(--warn);background:#e0a63a1a}.sev-LOW{color:#6fd3a3;border-color:var(--ok);background:#3fb27f1a}.sev-NONE{color:var(--mut);border-color:var(--bd)}
.tg-FACT{color:#6fd3a3;border-color:var(--ok)}.tg-DERIVED{color:#9fb0ff;border-color:#5566cc}.tg-AI{color:#c4a8ff;border-color:#8a63d2}.tg-MISSING{color:#f0c060;border-color:var(--warn)}
.wx-funnel{display:flex;align-items:stretch;gap:6px;margin:6px 0 4px;flex-wrap:wrap}
.wx-stage{flex:1 1 150px;background:var(--s1);border:1px solid var(--bd);border-radius:12px;padding:14px 16px;position:relative}
.wx-stage .n{font-size:1.9rem;font-weight:700}.wx-stage .l{color:var(--mut);font-size:.82rem}
.wx-stage .bar{height:4px;border-radius:4px;background:var(--ai);margin-top:10px;opacity:.85}
.wx-stage:last-child{border-color:var(--hi)}.wx-stage:last-child .bar{background:var(--hi)}
.wx-arrow{align-self:center;color:var(--mut);font-size:1.2rem}
.wx-inc{background:var(--s1);border:1px solid var(--bd);border-left:4px solid var(--bd);border-radius:12px;padding:14px 16px;margin-bottom:10px}
.wx-inc.HIGH{border-left-color:var(--hi)}.wx-inc.CRITICAL{border-left-color:var(--crit)}.wx-inc.MEDIUM{border-left-color:var(--warn)}.wx-inc.LOW{border-left-color:var(--ok)}
.wx-inc .t{font-weight:650;font-size:1.02rem;margin:6px 0 4px}.wx-inc .m{color:var(--mut);font-size:.82rem}
.wx-risk{background:var(--s1);border:1px solid var(--bd);border-radius:14px;padding:18px}
.wx-risk .big{font-size:3rem;font-weight:750;line-height:1}.wx-risk .of{color:var(--mut);font-size:1.1rem}
.wx-conf{display:inline-block;margin-left:14px;padding:6px 12px;border:1px dashed var(--ai);border-radius:10px;color:#b5c0ff;font-size:.85rem}
.wx-fac{display:flex;align-items:center;gap:10px;margin:7px 0;font-size:.85rem}.wx-fac .nm{flex:0 0 190px;color:var(--tx)}
.wx-fac .tr{flex:1;height:8px;background:var(--s2);border-radius:6px;overflow:hidden}.wx-fac .fi{height:100%;background:var(--ai)}.wx-fac .v{flex:0 0 48px;text-align:right;color:var(--mut)}
.wx-note{color:var(--mut);font-size:.78rem;margin-top:10px}
.wx-human{background:#7c8cff14;border:1px solid #3a4590;border-radius:10px;padding:10px 14px;font-size:.85rem}
.wx-hdr{background:var(--s1);border:1px solid var(--bd);border-radius:14px;padding:16px 18px;margin-bottom:12px}
.wx-hdr .id{color:var(--mut);font-size:.8rem;letter-spacing:.5px}.wx-hdr .tt{font-size:1.35rem;font-weight:700;margin:4px 0 8px}
.wx-flow{color:var(--mut);font-size:.78rem;letter-spacing:.3px}
@media (max-width:700px){.wx-fac .nm{flex-basis:120px}.wx-risk .big{font-size:2.4rem}.wx-conf{margin:10px 0 0}}
</style>
"""

FLOW = "Observe → Detect → Correlate → Investigate → Enrich → Explain → Assess Risk → Recommend"
TAGS = {"FACT": "FACT", "DERIVED": "DERIVED", "AI": "AI INFERENCE", "MISSING": "MISSING EVIDENCE"}


def inject(st) -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def brand(st) -> None:
    st.markdown('<div class="wx-brand">🛡️ WebIntelX AI</div><div class="wx-sub">Security Intelligence</div>'
                '<div class="wx-health"><span class="wx-dot"></span>All systems operational</div>', unsafe_allow_html=True)


def page_header(st, title: str, sub: str) -> None:
    st.markdown(f'<p class="wx-h1">{_e(title)}</p><p class="wx-tag">{_e(sub)}</p>', unsafe_allow_html=True)


def sev(level: str | None) -> str:
    lv = (level or "NONE").upper()
    lv = lv if lv in ("CRITICAL", "HIGH", "MEDIUM", "LOW") else "NONE"
    return f'<span class="wx-pill sev-{lv}">{"● " if lv != "NONE" else ""}{_e(level or "NOT SCORED")}</span>'


def tag(kind: str) -> str:
    k = kind if kind in TAGS else "FACT"
    return f'<span class="wx-pill tg-{k}">{TAGS[k]}</span>'


def funnel(rows: list[dict]) -> str:
    top = max([r["count"] or 0 for r in rows] + [1])
    parts = []
    for i, r in enumerate(rows):
        n = r["count"] or 0
        w = max(4, round(100 * n / top)) if n else 2
        parts.append(f'<div class="wx-stage"><div class="n">{_e(f"{n:,}")}</div><div class="l">{_e(r["stage"])}</div><div class="bar" style="width:{w}%"></div></div>')
        if i < len(rows) - 1:
            parts.append('<div class="wx-arrow">→</div>')
    return f'<div class="wx-funnel" role="list">{"".join(parts)}</div>'


def incident_card(card: dict) -> str:
    lv = (card.get("risk_level") or "NONE").upper()
    score = "not scored" if card.get("risk_score") is None else f'{card["risk_score"]:.0f}/100'
    conf = "n/a" if card.get("confidence") is None else f'{round(card["confidence"] * 100)}%'
    res = ", ".join(card.get("affected_resources") or []) or "none recorded"
    extra = (" · SYNTHETIC data" if card.get("contains_synthetic") else "") + (f' · alert {_e(str(card.get("priority")))}' if card.get("has_alert") else "")
    return (f'<div class="wx-inc {lv}">{sev(card.get("risk_level"))} <span class="m">&nbsp;Risk {score} · Confidence {conf} · {_e(str(card.get("status")))}</span>'
            f'<div class="t">{_e(str(card.get("title")))}</div><div class="m">Affected: {_e(res)} · {_e(str(card.get("event_count") or "?"))} events{extra}</div></div>')


def incident_header(inc: dict) -> str:
    d = inc.get("details") or {}
    res = ", ".join(d.get("affected_resources") or []) or "none recorded"
    conf = inc.get("confidence")
    c = "n/a" if conf is None else f"{round(conf * 100)}%"
    return (f'<div class="wx-hdr"><div class="id">{_e(str(inc.get("incident_id")))} · STATUS {_e(str(inc.get("status")))}</div>'
            f'<div class="tt">{_e(str(inc.get("title")))}</div>{sev(inc.get("risk_level"))} '
            f'<span class="m" style="color:#8b94a7;font-size:.85rem">&nbsp;Risk {_e(str(inc.get("risk_score")))} · Confidence {c} · Affected: {_e(res)}</span>'
            f'<div class="wx-flow" style="margin-top:8px">{_e(FLOW)}</div></div>')


def risk_card(risk: dict, rows: list[dict]) -> str:
    if (risk or {}).get("status") != "ok":
        return '<div class="wx-risk">Risk has not been scored yet.</div>'
    mx = max([r.get("points") or 0 for r in rows] + [1])
    bars = "".join(f'<div class="wx-fac"><span class="nm">{_e(str(r["factor"]).replace("_", " "))}</span><span class="tr"><span class="fi" style="width:{round(100 * (r.get("points") or 0) / mx)}%;display:block"></span></span>'
                   f'<span class="v">{_e(str(r.get("points")))}</span></div>' for r in rows)
    conf = risk.get("confidence")
    return (f'<div class="wx-risk"><span class="big">{_e(str(risk.get("risk_score")))}</span><span class="of"> / 100</span> &nbsp;{sev(risk.get("risk_level"))}'
            f'<span class="wx-conf">Evidence confidence: {"n/a" if conf is None else _e(str(conf))}</span><div style="margin-top:14px">{bars}</div>'
            '<div class="wx-note">Risk is calculated from structured evidence and configured scoring factors. Confidence (evidence quality) is separate and is not a probability.</div></div>')


def human_note(text: str) -> str:
    return f'<div class="wx-human">🧑‍💻 <b>Analyst stays in control.</b> {_e(text)}</div>'


# ---------------------------------------------------------------- step 2: attack story + graph styling
_ET_TAG = {"observed": "FACT", "derived_metric": "DERIVED", "derived_indicator": "DERIVED", "derived_correlation": "DERIVED",
           "ai_inference": "AI", "missing_evidence": "MISSING"}
NODE_COLORS = {"observed": "#4f8cff", "derived": "#a78bfa", "ai_inference": "#f0c060", "missing_evidence": "#8b94a7"}
PLOT_BG = "rgba(0,0,0,0)"


def tag_for(evidence_type: str | None) -> str:
    return tag(_ET_TAG.get(evidence_type or "", "DERIVED")) if (evidence_type or "") != "system" else '<span class="wx-pill sev-NONE">PLATFORM</span>'


def node_color(evidence_type: str | None) -> str:
    et = evidence_type or ""
    return NODE_COLORS.get("derived" if et.startswith("derived") else et, "#6b7280")


def timeline(rows: list[dict]) -> str:
    """Vertical Attack Story. `rows` = vm.timeline_rows output. Evidence ids shown on every step (evidence-first)."""
    if not rows:
        return '<div class="wx-note">No timeline entries.</div>'
    items = []
    for i, r in enumerate(rows, 1):
        n = r.get("event_count") or 0
        items.append(
            f'<div class="wx-step"><div class="wx-num">{i}</div><div class="wx-sbody">'
            f'<div class="wx-st">{_e(str(r.get("label")))}</div>'
            f'<div class="wx-sm">{_e(str(r.get("timestamp")))} &nbsp;{tag_for(r.get("evidence_type"))}</div>'
            f'<div class="wx-sm">Evidence: {n} event(s) · {_e(str(r.get("event_ids_short") or "none"))}{" …" if r.get("event_ids_truncated") else ""}</div>'
            f'</div></div>')
    return f'<div class="wx-story">{"".join(items)}</div>'


def graph_legend() -> str:
    def dot(c, t):
        return f'<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{c};margin:0 5px 0 12px"></span>{t}'
    return ('<div class="wx-note">' + dot(NODE_COLORS["observed"], "Observed event") + dot(NODE_COLORS["derived"], "Derived relationship")
            + dot(NODE_COLORS["ai_inference"], "AI finding") + " &nbsp;· every node and edge traces to event IDs (hover).</div>")


CSS_STEP2 = """
<style>
.wx-story{border-left:2px solid var(--bd);margin-left:14px;padding-left:0}
.wx-step{display:flex;gap:14px;position:relative;margin:0 0 14px -15px}
.wx-num{flex:0 0 28px;height:28px;border-radius:50%;background:var(--s2);border:2px solid var(--ai);color:var(--tx);display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700}
.wx-sbody{background:var(--s1);border:1px solid var(--bd);border-radius:10px;padding:10px 14px;flex:1}
.wx-st{font-weight:650}.wx-sm{color:var(--mut);font-size:.8rem;margin-top:3px}
</style>
"""


def inject_step2(st) -> None:
    st.markdown(CSS_STEP2, unsafe_allow_html=True)
