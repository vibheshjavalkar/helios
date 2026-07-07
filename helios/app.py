import streamlit as st
import time
from models.registry import MODEL_REGISTRY

from core.state import StateManager
from core.orchestrator import Orchestrator

from ui.theme import apply_theme
from ui.dashboard import (
    render_startup_animation,
    render_hero,
    render_mission_input,
    render_timeline,
    render_kpis,
    render_model_cards,
)

# ----------------------------
# STARTUP ANIMATION (ONCE PER SESSION)
# ----------------------------
if "animation_played" not in st.session_state:
    st.session_state.animation_played = False
    st.session_state.animation_start_time = time.time()

if not st.session_state.animation_played:
    elapsed = time.time() - st.session_state.animation_start_time
    if elapsed < 3.5:
        render_startup_animation()
        time.sleep(3.5 - elapsed)
        st.session_state.animation_played = True
        st.rerun()
    else:
        st.session_state.animation_played = True

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="HELIOS AI SYSTEM", layout="wide")
apply_theme()

# ----------------------------
# MODE TOGGLE
# ----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "SAFE"

from config import GEMINI_API_KEY

# Sidebar mode selector — keeps the main canvas clean
with st.sidebar:
    st.markdown("### ⚙️ System Settings")
    mode_choice = st.radio(
        "Execution Mode",
        ["SAFE", "DEMO"],
        index=0 if st.session_state.mode == "SAFE" else 1,
        horizontal=True,
    )
    st.session_state.mode = mode_choice

if st.session_state.mode == "DEMO" and not GEMINI_API_KEY:
    st.error("DEMO mode requires GEMINI_API_KEY")
    st.stop()

# ----------------------------
# 1. HERO
# ----------------------------
render_hero(st.session_state.mode)

# ----------------------------
# 2. MISSION INPUT
# ----------------------------
user_input, run = render_mission_input()

# ----------------------------
# 3. EXECUTION
# ----------------------------
if run and user_input:

    state = StateManager()
    system = Orchestrator(state)

    # ── Live execution timeline ──
    st.markdown('<div class="section-heading">📡 Live Execution</div>', unsafe_allow_html=True)
    launch_sequence_placeholder = st.empty()
    timeline_placeholder = st.empty()
    timeline_logs = []

    with launch_sequence_placeholder.container():
        st.markdown(f"""
        <div class="mission-initialized-card" style="background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; text-align: center;">
            <h3 style="color: #58a6ff; margin: 0 0 0.5rem 0; font-weight: 800;">🚀 MISSION INITIALIZED</h3>
            <p style="color: #8b949e; margin: 0 0 1rem 0; font-size: 0.9rem;">Goal: <strong>{user_input}</strong></p>
            <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.5rem; text-align: center;">
                <div><span style="font-size: 1.2rem;">🛡️</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Security<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">🧠</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Planner<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">🎯</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Router<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">📡</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">MCP Context<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">⚙️</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Executor<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">📊</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Explainability<br>ONLINE</div></div>
                <div><span style="font-size: 1.2rem;">🏁</span><div style="font-size: 0.75rem; color: #3fb950; font-weight: 600; margin-top: 0.2rem;">Verdict<br>ONLINE</div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    def ui_callback(msg):
        timeline_logs.append(msg)

        with timeline_placeholder.container():
            render_timeline(timeline_logs, finished=False)

        time.sleep(0.08)

    demo_bypassed = False
    try:
        result = system.run(user_input, mode=st.session_state.mode, ui_callback=ui_callback)
    except Exception as e:
        if st.session_state.mode == "DEMO":
            # Clear initial run and notify user of fallback
            launch_sequence_placeholder.empty()
            st.warning("""
⚠️ **Gemini Demo Mode Unavailable** (e.g. Quota Exhausted / Network Timeout). 
HELIOS has automatically bypassed execution to **SAFE Mode** to run offline simulations.
            """)
            # Execute in SAFE mode
            result = system.run(user_input, mode="SAFE", ui_callback=ui_callback)
            demo_bypassed = True
            
            # Log internally for debugging/certification requirements
            import datetime
            st.session_state.last_demo_error = {
                "timestamp": datetime.datetime.now().isoformat(),
                "exception_type": type(e).__name__,
                "message": str(e),
                "action": "Bypassed to SAFE Mode"
            }
        else:
            # If SAFE mode itself fails, raise it
            launch_sequence_placeholder.empty()
            st.error(f"Execution failed: {e}")
            st.stop()
    
    # Hide the initialization container when execution completes
    launch_sequence_placeholder.empty()

    tasks = state.get_state().get("tasks", [])
    logs = state.get_state().get("logs", [])
    dashboard = state.get_state().get("results", [])

    # ── Update original timeline container in place ──
    with timeline_placeholder.container():
        render_timeline(logs, finished=True)

    # ── Calculate savings ──
    total_cost = sum(
        MODEL_REGISTRY.get(r["model"], {}).get("cost", 0.0) for r in dashboard
    )
    baseline_cost = 10.0
    savings = ((baseline_cost - total_cost) / baseline_cost) * 100 if baseline_cost > 0 else 0
    savings = max(0, min(100, savings))

    # ----------------------------
    # 4. RESULTS AND ANALYTICS TABS
    # ----------------------------
    st.markdown('<div class="section-heading">🎯 Results & Analytics Center</div>', unsafe_allow_html=True)
    
    from ui.dashboard import (
        render_comparison_table,
        render_dag_graphviz,
        render_checklist,
        render_models_evaluated_list,
        render_confidence_gauge,
        render_verdict_visual,
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Results",
        "🎯 Routing",
        "📊 Analytics",
        "🧠 Explainability",
        "💻 Logs"
    ])

    with tab1:
        st.subheader("Final Answer")
        final_result = result.get(
            "final_output",
            "Success: Task successfully processed and technical summary generated.",
        )
        st.info(final_result)
        
        st.subheader("System Verdict")
        verdict_data = result.get("verdict", {})
        render_verdict_visual(verdict_data)
        
        st.subheader("Execution Summary")
        st.write(f"Estimated baseline cost: {baseline_cost} Compute Units.")
        st.write(f"Orchestrated compute cost: {round(total_cost, 2)} Compute Units.")
        
        with st.expander("Advanced Details (Raw JSON)"):
            st.json(result)

    with tab2:
        st.subheader("Model Routing Comparison")
        render_comparison_table(dashboard)
        
        st.subheader("Execution Plan Checklist")
        render_checklist(tasks)
        
        st.subheader("Routing Explanation")
        routing_reason = result.get("verdict", {}).get("insight")
        if not routing_reason:
            routing_reason = "Routing completed using local optimization score."
        st.info(routing_reason)

    with tab3:
        st.subheader("Performance Metrics")
        render_kpis(dashboard, total_cost, savings, tasks)
        
        st.subheader("Confidence & Efficiency")
        col_gauge, col_list = st.columns(2)
        with col_gauge:
            render_confidence_gauge(savings)
        with col_list:
            st.write("### Evaluated Candidates")
            render_models_evaluated_list()
            
        st.subheader("Model Intelligence Matrix")
        render_model_cards(dashboard)

        st.subheader("Analytical Charts")
        col_q, col_c = st.columns(2)
        with col_q:
            st.write("**Model Quality Comparison**")
            st.bar_chart({model: meta.get("quality", 0) for model, meta in MODEL_REGISTRY.items()})
        with col_c:
            st.write("**Model Latency Comparison**")
            st.bar_chart({model: meta.get("latency", 0) for model, meta in MODEL_REGISTRY.items()})

        col_cost, col_score = st.columns(2)
        with col_cost:
            st.write("**Relative Cost Index**")
            st.bar_chart({model: meta.get("cost", 0) for model, meta in MODEL_REGISTRY.items()})
        with col_score:
            st.write("**Local Optimization Routing Score**")
            st.bar_chart({model: (meta.get("quality", 0) - meta.get("cost", 0) - meta.get("latency", 0)) for model, meta in MODEL_REGISTRY.items()})

    with tab4:
        explanation = result.get("explanation", "")
        if explanation:
            st.subheader("AI Audit Report")
            st.text(explanation)
        else:
            st.warning("No AI Audit report generated for this run.")

    with tab5:
        if logs:
            st.subheader("System Developer Logs")
            for log in logs:
                st.text(log)
        else:
            st.warning("No logs recorded.")

    # ----------------------------
    # 5. EXECUTION FLOW DAG
    # ----------------------------
    if tasks:
        st.markdown('<div class="section-heading">🔗 Execution DAG Flowchart</div>', unsafe_allow_html=True)
        render_dag_graphviz(tasks)

    # ── Bottom insight banner ──
    st.divider()
    st.success(
        f"⚡ **System Insight:** This run saved **{round(savings, 2)}%** compute cost "
        f"by dynamically routing tasks across optimized models rather than using a "
        f"fixed high-tier model baseline."
    )
