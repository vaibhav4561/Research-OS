import streamlit as st
import time
import requests

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchOS",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Mono', monospace;
    background-color: #080b0f;
    color: #e2e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #30f2c0; border-radius: 2px; }

.hero { display: flex; align-items: center; gap: 1.2rem; margin-bottom: 0.4rem; }
.hero-badge {
    background: #30f2c0; color: #080b0f;
    font-family: 'DM Mono', monospace; font-size: 0.65rem;
    font-weight: 400; letter-spacing: 0.18em;
    padding: 4px 10px; border-radius: 2px; text-transform: uppercase;
}
h1.brand {
    font-family: 'Syne', sans-serif; font-size: 3.2rem;
    font-weight: 800; letter-spacing: -0.03em; line-height: 1;
    color: #f0f6ff; margin: 0;
}
h1.brand span { color: #30f2c0; }
.subtitle {
    font-size: 0.8rem; color: #4a5568; letter-spacing: 0.06em;
    margin-bottom: 2.5rem; padding-left: 2px;
}
.rule { border: none; border-top: 1px solid #1a2332; margin: 1.5rem 0; }

.stTextInput > div > div > input {
    background: #0d1117 !important; border: 1px solid #1e2d3d !important;
    border-radius: 6px !important; color: #e2e8f0 !important;
    font-family: 'DM Mono', monospace !important; font-size: 0.9rem !important;
    padding: 0.75rem 1rem !important; caret-color: #30f2c0;
    transition: border-color 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #30f2c0 !important;
    box-shadow: 0 0 0 2px rgba(48,242,192,0.08) !important;
}
.stTextInput > label {
    font-family: 'DM Mono', monospace !important; font-size: 0.72rem !important;
    letter-spacing: 0.12em !important; color: #4a5568 !important;
    text-transform: uppercase;
}

.stButton > button {
    background: #30f2c0 !important; color: #080b0f !important;
    font-family: 'Syne', sans-serif !important; font-weight: 700 !important;
    font-size: 0.82rem !important; letter-spacing: 0.1em !important;
    text-transform: uppercase !important; border: none !important;
    border-radius: 6px !important; padding: 0.65rem 2rem !important;
    transition: all 0.2s !important; cursor: pointer;
}
.stButton > button:hover {
    background: #22d4a8 !important; transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(48,242,192,0.25) !important;
}

.step-card {
    background: #0d1117; border: 1px solid #1a2332;
    border-left: 3px solid #1a2332; border-radius: 8px;
    padding: 1.1rem 1.4rem; margin-bottom: 0.8rem;
    transition: border-left-color 0.3s, background 0.3s; position: relative;
}
.step-card.active  { border-left-color: #30f2c0; background: #0b1520; }
.step-card.done    { border-left-color: #30f2c0; opacity: 0.7; }
.step-card.running { border-left-color: #30f2c0; background: #0b1520; }
.step-card.error   { border-left-color: #f25c54; background: #140d0d; }
.step-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.25rem; }
.step-icon   { font-size: 1.05rem; width: 1.4rem; text-align: center; }
.step-title  { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 0.9rem; color: #f0f6ff; }
.step-meta   { font-size: 0.7rem; color: #4a5568; letter-spacing: 0.06em; padding-left: 2.15rem; }
.step-status {
    position: absolute; right: 1.2rem; top: 50%; transform: translateY(-50%);
    font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase;
}
.step-status.running { color: #30f2c0; }
.step-status.done    { color: #30f2c0; }
.step-status.error   { color: #f25c54; }
.step-status.idle    { color: #2a3a4a; }

.panel-label { font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; color: #30f2c0; margin-bottom: 0.5rem; padding-left: 2px; }
.output-box {
    background: #0d1117; border: 1px solid #1a2332; border-radius: 8px;
    padding: 1.2rem 1.4rem; font-size: 0.82rem; line-height: 1.75;
    color: #a0aec0; max-height: 320px; overflow-y: auto;
    white-space: pre-wrap; word-break: break-word; font-family: 'DM Mono', monospace;
}
.report-box {
    background: #0b1520; border: 1px solid #1e2d3d; border-top: 2px solid #30f2c0;
    border-radius: 8px; padding: 1.6rem 1.8rem; font-size: 0.88rem; line-height: 1.9;
    color: #cbd5e0; white-space: pre-wrap; word-break: break-word; font-family: 'DM Mono', monospace;
}
.feedback-box {
    background: #0d1117; border: 1px solid #1a2332; border-top: 2px solid #f6c90e;
    border-radius: 8px; padding: 1.4rem 1.6rem; font-size: 0.84rem; line-height: 1.85;
    color: #a0aec0; white-space: pre-wrap; word-break: break-word; font-family: 'DM Mono', monospace;
}

.metric-row { display: flex; gap: 1rem; margin: 1.5rem 0; }
.metric-pill {
    flex: 1; background: #0d1117; border: 1px solid #1a2332;
    border-radius: 6px; padding: 0.9rem 1.1rem; text-align: center;
}
.metric-val  { font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 800; color: #30f2c0; line-height: 1; margin-bottom: 0.25rem; }
.metric-key  { font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase; color: #4a5568; }

.success-bar {
    background: linear-gradient(90deg, #0d2e27 0%, #0b1520 100%);
    border: 1px solid #30f2c0; border-radius: 6px;
    padding: 0.9rem 1.4rem; font-size: 0.78rem; color: #30f2c0;
    letter-spacing: 0.06em; margin: 1rem 0;
    display: flex; align-items: center; gap: 0.6rem;
}
.section-heading {
    font-family: 'Syne', sans-serif; font-size: 1.05rem; font-weight: 700;
    color: #f0f6ff; margin: 2rem 0 1rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.section-heading::after {
    content: ''; flex: 1; height: 1px; background: #1a2332; margin-left: 0.5rem;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ─────────────────────────────────────────────────────────────────────
def step_card(icon, title, meta, status="idle", key=""):
    labels = {"idle": "○ waiting", "running": "◉ running…", "done": "✓ done", "error": "✕ failed"}
    label  = labels.get(status, "○ waiting")
    st.markdown(f"""
    <div class="step-card {status}">
        <div class="step-header">
            <span class="step-icon">{icon}</span>
            <span class="step-title">{title}</span>
        </div>
        <div class="step-meta">{meta}</div>
        <span class="step-status {status}">{label}</span>
    </div>""", unsafe_allow_html=True)


def output_panel(label, content, box_class="output-box"):
    st.markdown(f'<div class="panel-label">{label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="{box_class}">{content}</div>', unsafe_allow_html=True)


# ── Session state ────────────────────────────────────────────────────────────────
for k in ["running", "done", "state", "elapsed", "error"]:
    if k not in st.session_state:
        st.session_state[k] = None if k in ("state", "error") else False


# ── Header ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero"><span class="hero-badge">AI Research</span></div>
<h1 class="brand">Research<span>OS</span></h1>
<p class="subtitle">// autonomous search · scrape · synthesise · critique</p>
""", unsafe_allow_html=True)
st.markdown('<hr class="rule">', unsafe_allow_html=True)


# ── Input row ────────────────────────────────────────────────────────────────────
col_in, col_btn = st.columns([5, 1], gap="medium")
with col_in:
    topic = st.text_input("RESEARCH TOPIC", placeholder="e.g. Quantum computing breakthroughs in 2025")
with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    run_clicked = st.button("▶  Run", use_container_width=True)


# ── Pipeline execution ───────────────────────────────────────────────────────────
if run_clicked and topic.strip():
    st.session_state.running = True
    st.session_state.done    = False
    st.session_state.state   = None
    st.session_state.error   = None

    st.markdown('<hr class="rule">', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">⬡ Pipeline</div>', unsafe_allow_html=True)

    placeholders = [st.empty() for _ in range(4)]
    steps = [
        ("🔍", "Search Agent",  "querying web for recent, reliable sources"),
        ("📖", "Reader Agent",  "scraping top URL for deeper content"),
        ("✍️",  "Writer Chain",  "synthesising findings into a structured report"),
        ("🧠", "Critic Chain",  "reviewing report quality & accuracy"),
    ]

    def render_steps(active):
        for i, (icon, title, meta) in enumerate(steps):
            s = "done" if i < active else "running" if i == active else "idle"
            with placeholders[i]:
                step_card(icon, title, meta, s, str(i))

    spinner_ph = st.empty()
    t0 = time.time()

    try:

        with st.spinner("Research pipeline is running..."):
            response = requests.post(
                "http://127.0.0.1:8000/research/",
                json={
                    "query": topic
                }
            )

        response.raise_for_status()

        data = response.json()

        search_results = data["search_results"]
        scraped_content = data["scraped_content"]
        report = data["report"]
        feedback = data["feedback"]

        st.session_state.state = {
            "search_results": search_results,
            "scraped_content": scraped_content,
            "report": report,
            "feedback": feedback,
        }
        s = st.session_state.state

        st.session_state.elapsed = round(time.time() - t0, 1)
        st.session_state.done = True
        st.session_state.running = False

    except Exception as e:
        spinner_ph.empty()
        st.session_state.error   = str(e)
        st.session_state.running = False

elif run_clicked:
    st.warning("Please enter a research topic first.")


# ── Error ────────────────────────────────────────────────────────────────────────
if st.session_state.error:
    st.markdown(f"""
    <div class="step-card error" style="margin-top:1.5rem;">
        <div class="step-header">
            <span class="step-icon">✕</span>
            <span class="step-title">Pipeline error</span>
        </div>
        <div class="step-meta" style="color:#f25c54;">{st.session_state.error}</div>
    </div>""", unsafe_allow_html=True)


# ── Results ───────────────────────────────────────────────────────────────────────
if st.session_state.done and st.session_state.state:
    s       = st.session_state.state
    elapsed = st.session_state.elapsed
    wc      = len(s.get("report", "").split())
    sc      = len(s.get("scraped_content", "").split())

    st.markdown(f'<div class="success-bar">✓ &nbsp; Pipeline completed in {elapsed}s — all 4 stages passed</div>',
                unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-pill"><div class="metric-val">{elapsed}s</div><div class="metric-key">Total time</div></div>
        <div class="metric-pill"><div class="metric-val">{wc}</div><div class="metric-key">Report words</div></div>
        <div class="metric-pill"><div class="metric-val">{sc}</div><div class="metric-key">Scraped words</div></div>
        <div class="metric-pill"><div class="metric-val">4</div><div class="metric-key">Stages passed</div></div>
    </div>""", unsafe_allow_html=True)

    with st.expander("🔍  Search Results  ·  raw output", expanded=False):
        output_panel("SEARCH AGENT OUTPUT", s.get("search_results", "—"))

    with st.expander("📖  Scraped Content  ·  raw output", expanded=False):
        output_panel("READER AGENT OUTPUT", s.get("scraped_content", "—"))

    st.markdown('<hr class="rule">', unsafe_allow_html=True)

    st.markdown('<div class="section-heading">✍️  Final Report</div>', unsafe_allow_html=True)
    output_panel("GENERATED REPORT", s.get("report", "—"), "report-box")

    st.markdown('<div class="section-heading" style="margin-top:1.5rem;">🧠  Critic Feedback</div>',
                unsafe_allow_html=True)
    output_panel("QUALITY REVIEW", s.get("feedback", "—"), "feedback-box")

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, _ = st.columns([1, 1, 4], gap="small")
    with c1:
        st.download_button("⬇  Report", s.get("report",""),
            file_name=f"report_{topic[:30].replace(' ','_')}.txt", mime="text/plain", use_container_width=True)
    with c2:
        full = (f"TOPIC: {topic}\n\n{'='*60}\nSEARCH RESULTS\n{'='*60}\n{s.get('search_results','')}\n\n"
                f"{'='*60}\nSCRAPED CONTENT\n{'='*60}\n{s.get('scraped_content','')}\n\n"
                f"{'='*60}\nFINAL REPORT\n{'='*60}\n{s.get('report','')}\n\n"
                f"{'='*60}\nCRITIC FEEDBACK\n{'='*60}\n{s.get('feedback','')}\n")
        st.download_button("⬇  Full Export", full,
            file_name=f"full_{topic[:30].replace(' ','_')}.txt", mime="text/plain", use_container_width=True)


# ── Idle hint ─────────────────────────────────────────────────────────────────────
if not st.session_state.done and not st.session_state.running and not st.session_state.error:
    st.markdown("""
    <div style="margin-top:3rem;text-align:center;color:#1e2d3d;font-size:0.75rem;letter-spacing:0.12em;">
        ↑ &nbsp; ENTER A TOPIC AND PRESS RUN TO START THE PIPELINE
    </div>""", unsafe_allow_html=True)