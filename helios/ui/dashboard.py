import streamlit as st
from models.registry import MODEL_REGISTRY


def render_startup_animation():
    """Render cinematic startup animation sequence with CSS particle effects and typography."""
    st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;900&display=swap');
.startup-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #000000;
    z-index: 999999;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
}
.particle {
    position: absolute;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    top: 50%;
    transform: translateY(-50%);
}
.left-particle {
    background: #58a6ff;
    left: -100px;
    box-shadow: 0 0 20px #58a6ff, 0 0 40px #58a6ff, 0 0 60px #58a6ff;
    animation: moveLeft 1.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
.right-particle {
    background: #e3b341;
    right: -100px;
    box-shadow: 0 0 20px #e3b341, 0 0 40px #e3b341, 0 0 60px #e3b341;
    animation: moveRight 1.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes moveLeft {
    to { left: 50%; transform: translate(-50%, -50%); }
}
@keyframes moveRight {
    to { right: 50%; transform: translate(50%, -50%); }
}
.starburst {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: radial-gradient(circle, #ffffff 0%, rgba(88,166,255,1) 30%, rgba(227,179,65,0.8) 60%, rgba(0,0,0,0) 100%);
    animation: burst 0.8s 1.2s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    z-index: 1000000;
}
@keyframes burst {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
    100% { transform: translate(-50%, -50%) scale(100); opacity: 0; }
}
.reveal-container {
    text-align: center;
    opacity: 0;
    animation: fadeInText 1.5s 1.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    z-index: 1000001;
}
@keyframes fadeInText {
    from { opacity: 0; transform: scale(0.92); filter: blur(10px); }
    to { opacity: 1; transform: scale(1); filter: blur(0); }
}
.logo-text {
    font-weight: 900;
    font-size: 5rem;
    letter-spacing: 12px;
    margin: 0;
    background: linear-gradient(135deg, #58a6ff 0%, #3fb950 50%, #58a6ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textGlow 3s infinite alternate ease-in-out;
}
@keyframes textGlow {
    0% { filter: drop-shadow(0 0 10px rgba(88,166,255,0.4)) drop-shadow(0 0 20px rgba(88,166,255,0.2)); }
    100% { filter: drop-shadow(0 0 25px rgba(88,166,255,0.8)) drop-shadow(0 0 50px rgba(88,166,255,0.4)); }
}
.subtitle-text {
    font-weight: 300;
    font-size: 1.15rem;
    color: #8b949e;
    letter-spacing: 3px;
    margin-top: 1rem;
    text-transform: uppercase;
}
</style>
<div class="startup-wrapper">
<div class="particle left-particle"></div>
<div class="particle right-particle"></div>
<div class="starburst"></div>
<div class="reveal-container">
<h1 class="logo-text">HELIOS</h1>
<p class="subtitle-text">Compute-Aware Multi-Agent Orchestration System</p>
</div>
</div>""", unsafe_allow_html=True)


def render_hero(mode):
    """Render the hero header with title, subtitle, and status badges."""
    from config import GEMINI_API_KEY
    mode_badge = (
        '<span class="badge badge-demo">🟡 DEMO MODE</span>'
        if mode == "DEMO"
        else '<span class="badge badge-safe">🟢 SAFE MODE</span>'
    )
    gemini_status = (
        '<span class="badge badge-connected">🟢 Gemini Connected</span>'
        if GEMINI_API_KEY
        else '<span class="badge badge-demo">🔴 Gemini Missing</span>'
    )
    runtime_status = (
        '<span class="badge badge-active">⚡ Gemini Available</span>'
        if GEMINI_API_KEY
        else '<span class="badge badge-demo">⚠️ Simulation Only</span>'
    )
    st.markdown(f"""<div class="hero-section">
<div class="hero-title">HELIOS</div>
<p class="hero-subtitle">Compute-Aware Multi-Agent Orchestration System</p>
<div class="badge-row">
{mode_badge}
{gemini_status}
{runtime_status}
</div>
</div>""", unsafe_allow_html=True)


def render_mission_input():
    """Render the centered mission input card. Returns (user_input, run_clicked)."""
    st.markdown('<div class="mission-card"><h3>🎯 Mission Brief</h3><p>Describe your AI task and the system will orchestrate an optimal execution plan.</p></div>', unsafe_allow_html=True)
    
    # Preset scenarios buttons
    cols_preset = st.columns(4)
    if "mission_input" not in st.session_state:
        st.session_state.mission_input = ""

    with cols_preset[0]:
        if st.button("🚀 Launch HELIOS Demo Scenario", use_container_width=True):
            st.session_state.mission_input = "Analyze the efficiency of a distributed AI system"
    with cols_preset[1]:
        if st.button("🧬 Scientific Research", use_container_width=True):
            st.session_state.mission_input = "Analyze quantum computing applications"
    with cols_preset[2]:
        if st.button("📊 Business Optimization", use_container_width=True):
            st.session_state.mission_input = "Optimize a company's workflow to reduce operational cost"
    with cols_preset[3]:
        if st.button("🌱 Complex Analysis", use_container_width=True):
            st.session_state.mission_input = "Analyze renewable energy adoption strategies"

    user_input = st.text_area(
        "Describe your AI task", 
        height=100, 
        label_visibility="collapsed", 
        placeholder="e.g. Research quantum computing breakthroughs and generate a technical summary...",
        value=st.session_state.mission_input
    )
    col_left, col_center, col_right = st.columns([2, 1, 2])
    with col_center:
        run = st.button("🚀 Run Orchestration", use_container_width=True)
    return user_input, run


def render_timeline(logs, finished=False):
    """Render a visual execution timeline from log messages."""
    stage_map = [
        ("🛡️", "Security", "SECURITY"),
        ("🧠", "Planner", "Planner"),
        ("🎯", "Router", "ROUTER"),
        ("📡", "MCP Context", "MCP"),
        ("⚙️", "Execution", "EXECUTION"),
        ("📊", "Explainability", "Audit"),
        ("🏁", "Verdict", "Verdict"),
    ]
    html = '<div class="timeline-container" style="display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px; margin: auto;">'
    logs_text = "\n".join(logs)
    
    # Find active stage index
    active_idx = -1
    if not finished:
        for idx, (_, _, keyword) in enumerate(stage_map):
            if keyword.lower() in logs_text.lower():
                active_idx = idx

    for idx, (icon, name, keyword) in enumerate(stage_map):
        is_matched = keyword.lower() in logs_text.lower()
        if is_matched:
            if idx == active_idx:
                css_class = "active"
                status = "🔄 Running"
            else:
                css_class = "done"
                status = "✅ Complete"
        else:
            css_class = "pending"
            status = "⏳ Pending"
            
        html += f'<div class="timeline-stage {css_class}"><span class="timeline-icon">{icon}</span><span class="timeline-name">{name}</span><span class="timeline-status">{status}</span></div>'
        
        if idx < len(stage_map) - 1:
            html += '<div style="text-align: center; color: #30363d; margin: -0.1rem 0; font-size: 0.8rem;">↓</div>'
            
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_kpis(dashboard, total_cost, savings, tasks):
    """Render the 7 KPI metric cards."""
    models_evaluated = len(MODEL_REGISTRY)
    avg_latency = 0
    avg_quality = 0
    if dashboard:
        avg_latency = round(sum(MODEL_REGISTRY.get(r["model"], {}).get("latency", 0) for r in dashboard) / len(dashboard), 1)
        avg_quality = round(sum(MODEL_REGISTRY.get(r["model"], {}).get("quality", 0) for r in dashboard) / len(dashboard), 1)
    
    confidence = round(100 - (total_cost * 2))  # Local derivation

    st.markdown(f"""<div class="kpi-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 1rem 0;">
<div class="kpi-card" style="background:#161b22; border:1px solid #30363d; border-radius:10px; padding:1rem; text-align:center;">
    <div style="font-size:1.5rem;">📋</div>
    <div style="font-size:1.5rem; font-weight:800; color:#58a6ff; margin:0.2rem 0;">{len(tasks)}</div>
    <div style="font-size:0.75rem; color:#8b949e; text-transform:uppercase;">Tasks Created</div>
</div>
<div class="kpi-card" style="background:#161b22; border:1px solid #30363d; border-radius:10px; padding:1rem; text-align:center;">
    <div style="font-size:1.5rem;">⭐</div>
    <div style="font-size:1.5rem; font-weight:800; color:#3fb950; margin:0.2rem 0;">{avg_quality}/10</div>
    <div style="font-size:0.75rem; color:#8b949e; text-transform:uppercase;">Average Quality</div>
</div>
<div class="kpi-card" style="background:#161b22; border:1px solid #30363d; border-radius:10px; padding:1rem; text-align:center;">
    <div style="font-size:1.5rem;">⚡</div>
    <div style="font-size:1.5rem; font-weight:800; color:#e3b341; margin:0.2rem 0;">{avg_latency}s</div>
    <div style="font-size:0.75rem; color:#8b949e; text-transform:uppercase;">Estimated Latency</div>
</div>
<div class="kpi-card" style="background:#161b22; border:1px solid #30363d; border-radius:10px; padding:1rem; text-align:center;">
    <div style="font-size:1.5rem;">📉</div>
    <div style="font-size:1.5rem; font-weight:800; color:#bc8cff; margin:0.2rem 0;">{round(savings)}%</div>
    <div style="font-size:0.75rem; color:#8b949e; text-transform:uppercase;">Estimated Reduction</div>
</div>
</div>""", unsafe_allow_html=True)


def render_confidence_gauge(savings):
    """Render a pure SVG circular confidence gauge."""
    stroke_dash = int((savings / 100) * 283)
    gauge_html = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 1rem 0;">
        <svg width="200" height="120" viewBox="0 0 200 120">
            <path d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="#21262d" stroke-width="15" stroke-linecap="round"/>
            <path d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="url(#gauge-grad)" stroke-width="15" stroke-linecap="round"
                  stroke-dasharray="283" stroke-dashoffset="{283 - stroke_dash}"/>
            <defs>
                <linearGradient id="gauge-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#f85149" />
                    <stop offset="50%" stop-color="#e3b341" />
                    <stop offset="100%" stop-color="#3fb950" />
                </linearGradient>
            </defs>
            <text x="100" y="90" text-anchor="middle" fill="#e6edf3" font-size="28" font-weight="bold" font-family="'Inter', sans-serif">{round(savings)}%</text>
        </svg>
        <div style="font-size: 0.85rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-top: -10px;">Confidence Score</div>
    </div>
    """
    st.markdown(gauge_html, unsafe_allow_html=True)


def render_models_evaluated_list():
    """Render list of models evaluated with status indicators."""
    html = """
    <div style="display: flex; flex-direction: column; gap: 0.5rem; text-align: left; padding: 1rem; background: #161b22; border: 1px solid #30363d; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #3fb950;">🟢</span> <strong style="color:#e6edf3;">Gemini 2.5 Flash</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Real LLM)</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #e3b341;">🟡</span> <strong style="color:#e6edf3;">GPT-4o</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Simulated)</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #e3b341;">🟡</span> <strong style="color:#e6edf3;">Claude</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Simulated)</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #e3b341;">🟡</span> <strong style="color:#e6edf3;">Perplexity</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Simulated)</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #58a6ff;">🔵</span> <strong style="color:#e6edf3;">Ollama Llama3</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Connector Stub)</span></div>
        <div style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: #58a6ff;">🔵</span> <strong style="color:#e6edf3;">Mistral Local</strong> <span style="font-size: 0.75rem; color:#8b949e;">(Connector Stub)</span></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_model_cards(dashboard):
    """Render the model routing visualization cards with glowing selected state."""
    selected_models = {r["model"] for r in dashboard}
    cards_html = '<div class="model-grid">'
    for model, meta in MODEL_REGISTRY.items():
        mtype = meta.get("type", "unknown")
        if mtype == "real":
            type_label = "🟢 REAL LLM"
        elif mtype == "simulated":
            type_label = "🟡 SIMULATED MODEL"
        else:
            type_label = "🔵 CONNECTOR STUB"

        sel_class = "selected" if model in selected_models else ""
        sel_tag = '<span class="selected-tag">✓ SELECTED</span>' if model in selected_models else ""

        quality = meta.get("quality", 0)
        cost = meta.get("cost", 0)
        latency = meta.get("latency", 0)

        quality_pct = int((quality / 10) * 100)
        cost_pct = int((cost / 10) * 100)
        latency_pct = int((latency / 5) * 100)

        cards_html += f'<div class="model-card {sel_class}">' \
                      f'{sel_tag}' \
                      f'<div class="model-name">{model}</div>' \
                      f'<div class="model-provider">{meta.get("provider", "unknown").upper()}</div>' \
                      f'<span class="model-type-badge">{type_label}</span>' \
                      f'<div class="bar-row"><span class="bar-label">Quality</span><div class="bar-track"><div class="bar-fill bar-fill-quality" style="width:{quality_pct}%"></div></div></div>' \
                      f'<div class="bar-row"><span class="bar-label">Cost Index</span><div class="bar-track"><div class="bar-fill bar-fill-cost" style="width:{cost_pct}%"></div></div></div>' \
                      f'<div class="bar-row"><span class="bar-label">Latency</span><div class="bar-track"><div class="bar-fill bar-fill-latency" style="width:{latency_pct}%"></div></div></div>' \
                      f'</div>'
    cards_html += "</div>"
    st.markdown(cards_html, unsafe_allow_html=True)


def render_verdict_visual(verdict_data):
    """Render a premium visual layout for the System Verdict instead of raw JSON."""
    verdict = verdict_data.get("verdict", "N/A")
    score = verdict_data.get("efficiency_score", 0.0)
    insight = verdict_data.get("insight", "")
    
    if "Highly" in verdict:
        color = "#3fb950"
        bg_color = "rgba(63, 185, 80, 0.1)"
    elif "Moderately" in verdict:
        color = "#e3b341"
        bg_color = "rgba(227, 179, 65, 0.1)"
    else:
        color = "#f85149"
        bg_color = "rgba(248, 81, 73, 0.1)"
        
    html = f'<div style="background: {bg_color}; border: 1px solid {color}; border-radius: 10px; padding: 1.5rem; margin: 1rem 0;">' \
           f'<h3 style="color: {color}; margin: 0 0 0.5rem 0; font-weight: 800;">🏆 SYSTEM VERDICT: {verdict.upper()}</h3>' \
           f'<div style="font-size: 1.25rem; font-weight: bold; color: #e6edf3; margin-bottom: 0.5rem;">' \
           f'Efficiency Score: <span style="color: {color}; font-size: 1.5rem;">{score}%</span>' \
           f'</div>' \
           f'<p style="color: #8b949e; margin: 0; font-size: 0.9rem; font-style: italic;">' \
           f'Insight: {insight}' \
           f'</p>' \
           f'</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_comparison_table(dashboard):
    """Render a premium HTML table comparing all models with selected model highlighting."""
    selected_models = {r["model"] for r in dashboard}
    
    rows_html = ""
    for model, meta in MODEL_REGISTRY.items():
        is_selected = model in selected_models
        style = "background-color: #1b2620; border-left: 4px solid #3fb950;" if is_selected else ""
        status = "Active Selection" if is_selected else "Idle"
        
        rows_html += f'<tr style="{style} border-bottom: 1px solid #21262d;">' \
                     f'<td style="padding: 10px; color: #e6edf3;"><strong>{model}</strong></td>' \
                     f'<td style="padding: 10px; color: #8b949e;">{meta.get("provider", "unknown").upper()}</td>' \
                     f'<td style="padding: 10px; color: #8b949e;">{meta.get("type", "unknown").upper()}</td>' \
                     f'<td style="padding: 10px; color: #3fb950; font-weight: bold;">{meta.get("quality", 0)}/10</td>' \
                     f'<td style="padding: 10px; color: #bc8cff;">{meta.get("latency", 0)}s</td>' \
                     f'<td style="padding: 10px; color: #e3b341;">{meta.get("cost", 0)} Compute Units</td>' \
                     f'<td style="padding: 10px; color: #58a6ff;">{status}</td>' \
                     f'</tr>'
        
    table_html = f'<table style="width: 100%; border-collapse: collapse; text-align: left; background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; overflow: hidden;">' \
                 f'<thead>' \
                 f'<tr style="background-color: #21262d; border-bottom: 2px solid #30363d;">' \
                 f'<th style="padding: 12px; color: #e6edf3;">Model</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Provider</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Execution Type</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Quality</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Latency</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Cost Index</th>' \
                 f'<th style="padding: 12px; color: #e6edf3;">Status</th>' \
                 f'</tr>' \
                 f'</thead>' \
                 f'<tbody>' \
                 f'{rows_html}' \
                 f'</tbody>' \
                 f'</table>'
    st.markdown(table_html, unsafe_allow_html=True)


def render_dag_graphviz(tasks):
    """Render a visual execution flow using Graphviz."""
    dot_code = """
    digraph G {
        bgcolor="transparent";
        rankdir=TB;
        node [style="filled,rounded", fillcolor="#161b22", color="#30363d", fontcolor="#e6edf3", fontname="Inter", shape=box, width=3, height=0.5];
        edge [color="#30363d", arrowsize=0.6];
        
        "User Goal" [fillcolor="#1c2430", color="#58a6ff", fontcolor="#58a6ff", style="filled,rounded,bold"];
        "Verdict" [fillcolor="#1b2620", color="#3fb950", fontcolor="#3fb950", style="filled,rounded,bold"];
        
        "User Goal" -> "Security";
        "Security" -> "Planner";
        "Planner" -> "Router";
        "Router" -> "Model Comparison";
        "Model Comparison" -> "Execution";
        "Execution" -> "Explainability";
        "Explainability" -> "Verdict";
    }
    """
    st.graphviz_chart(dot_code)


def render_checklist(tasks):
    """Render execution plan checklist."""
    html = '<div style="display: flex; flex-direction: column; gap: 0.6rem; padding: 1rem; background: #161b22; border: 1px solid #30363d; border-radius: 8px;">'
    for task in tasks:
        name = task.get("name", "Unknown Task")
        html += f'<div style="display: flex; align-items: center; gap: 0.6rem; color: #e6edf3;"><span style="color:#3fb950; font-weight:bold;">✓</span> <span>{name}</span></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
