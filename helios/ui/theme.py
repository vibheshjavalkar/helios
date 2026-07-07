import streamlit as st

def apply_theme():
    """Inject custom dark operations CSS into the Streamlit app."""
    st.markdown("""
    <style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .stApp {
        background-color: transparent !important;
        color: #e6edf3;
        font-family: 'Inter', sans-serif;
    }

    /* Hide default Streamlit header / footer */
    header[data-testid="stHeader"] { background: transparent; }
    #MainMenu, footer { visibility: hidden; }

    /* ── Section Containers ── */
    .hero-section {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem 1rem;
        border-bottom: 1px solid #21262d;
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #58a6ff 0%, #3fb950 50%, #58a6ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #8b949e;
        font-weight: 400;
        margin-top: 0;
    }

    /* ── Status Badges ── */
    .badge-row {
        display: flex;
        justify-content: center;
        gap: 0.75rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .badge-demo { background: rgba(210,153,34,0.15); color: #e3b341; border: 1px solid rgba(210,153,34,0.3); }
    .badge-safe { background: rgba(63,185,80,0.15); color: #3fb950; border: 1px solid rgba(63,185,80,0.3); }
    .badge-connected { background: rgba(63,185,80,0.15); color: #3fb950; border: 1px solid rgba(63,185,80,0.3); }
    .badge-active { background: rgba(88,166,255,0.15); color: #58a6ff; border: 1px solid rgba(88,166,255,0.3); }

    /* ── Mission Input Card ── */
    .mission-card {
        background: rgba(22, 27, 34, 0.6) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-radius: 12px;
        padding: 1.8rem 2rem;
        max-width: 720px;
        margin: 0 auto 2rem auto;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    .mission-card h3 {
        color: #e6edf3;
        margin: 0 0 0.5rem 0;
        font-weight: 700;
    }
    .mission-card p {
        color: #8b949e;
        margin: 0 0 1rem 0;
        font-size: 0.88rem;
    }

    /* ── KPI Metric Cards (5 Columns) ── */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin: 1.5rem 0;
    }
    .kpi-card {
        background: rgba(22, 27, 34, 0.6) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(88, 166, 255, 0.4) !important;
        box-shadow: 0 12px 30px rgba(88, 166, 255, 0.1);
    }
    .kpi-icon { font-size: 1.6rem; }
    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #58a6ff;
        margin: 0.3rem 0;
    }
    .kpi-label {
        font-size: 0.78rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    /* ── Timeline ── */
    @keyframes stagePulse {
        0% { background: rgba(22, 27, 34, 0.6); box-shadow: 0 0 0 0 rgba(88, 166, 255, 0.2); }
        50% { background: rgba(28, 38, 53, 0.8); box-shadow: 0 0 8px 2px rgba(88, 166, 255, 0.4); }
        100% { background: rgba(22, 27, 34, 0.6); box-shadow: 0 0 0 0 rgba(88, 166, 255, 0.2); }
    }
    .timeline-stage {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.6rem 1rem;
        margin: 0.25rem 0;
        background: rgba(22, 27, 34, 0.6) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-left: 3px solid #30363d;
        border-top: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-right: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-bottom: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-radius: 0 8px 8px 0;
        font-size: 0.88rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .timeline-stage.done { border-left-color: #3fb950; }
    .timeline-stage.active { 
        border-left-color: #58a6ff; 
        animation: stagePulse 1.5s infinite ease-in-out;
    }
    .timeline-icon { font-size: 1.2rem; width: 1.6rem; text-align: center; }
    .timeline-name { font-weight: 600; color: #e6edf3; }
    .timeline-status { color: #8b949e; font-size: 0.8rem; margin-left: auto; }

    /* ── Model Cards ── */
    .model-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    .model-card {
        background: rgba(22, 27, 34, 0.6) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(48, 54, 61, 0.4) !important;
        border-radius: 10px;
        padding: 1rem;
        position: relative;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .model-card:hover {
        transform: translateY(-2px);
        border-color: rgba(88, 166, 255, 0.4) !important;
        box-shadow: 0 12px 30px rgba(88, 166, 255, 0.1);
    }
    @keyframes selectScale {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    .model-card.selected { 
        border-color: #3fb950 !important; 
        box-shadow: 0 0 15px rgba(63,185,80,0.4);
        background: rgba(27, 38, 32, 0.8) !important;
        animation: selectScale 0.6s ease-in-out;
    }
    .model-name { font-weight: 700; font-size: 0.95rem; color: #e6edf3; margin-bottom: 0.3rem; }
    .model-provider { font-size: 0.75rem; color: #8b949e; }
    .model-type-badge {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 9999px;
        font-size: 0.68rem;
        font-weight: 600;
        margin: 0.5rem 0 0.6rem 0;
    }
    .type-real { background: rgba(63,185,80,0.15); color: #3fb950; }
    .type-sim { background: rgba(210,153,34,0.15); color: #e3b341; }
    .type-conn { background: rgba(88,166,255,0.15); color: #58a6ff; }

    .bar-row { display: flex; align-items: center; gap: 0.4rem; margin: 0.2rem 0; font-size: 0.75rem; }
    .bar-label { color: #8b949e; width: 50px; }
    .bar-track { flex: 1; height: 6px; background: #21262d; border-radius: 3px; overflow: hidden; }
    .bar-fill { height: 100%; border-radius: 3px; }
    .bar-fill-quality { background: linear-gradient(90deg, #3fb950, #58a6ff); }
    .bar-fill-cost { background: linear-gradient(90deg, #e3b341, #f85149); }
    .bar-fill-latency { background: linear-gradient(90deg, #58a6ff, #bc8cff); }

    .selected-tag {
        position: absolute;
        top: 8px; right: 8px;
        background: rgba(63,185,80,0.2);
        color: #3fb950;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 0.15rem 0.5rem;
        border-radius: 9999px;
    }

    /* ── DAG ── */
    .dag-container { text-align: center; margin: 1rem 0; }
    .dag-node {
        display: inline-block;
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 0.7rem 1.5rem;
        margin: 0.3rem auto;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .dag-arrow { color: #30363d; font-size: 1.2rem; }

    /* ── Section Headings ── */
    .section-heading {
        font-size: 1.1rem;
        font-weight: 700;
        color: #e6edf3;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin: 2rem 0 0.8rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #21262d;
    }

    /* ── Expanders & Tabs ── */
    div[data-testid="stExpander"] {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
    }
    div[data-testid="stExpander"] summary {
        font-weight: 600;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #238636, #2ea043);
        color: white;
        border: none;
        font-weight: 700;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        font-size: 0.95rem;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2ea043, #3fb950);
        box-shadow: 0 0 16px rgba(46,160,67,0.4);
    }

    /* ── Text area ── */
    .stTextArea textarea {
        background: #0d1117 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* ── Animations & Transitions ── */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .kpi-card, .model-card, .dag-node, .timeline-stage, div[data-testid="stExpander"], div[data-testid="stTab"] {
        animation: fadeIn 0.6s ease-out forwards;
    }

    .timeline-stage.done {
        border-left-color: #3fb950 !important;
        box-shadow: 0 0 10px rgba(63, 185, 80, 0.3) !important;
    }
    </style>
    <canvas id="stardust-canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; pointer-events: none; background: #0d1117;"></canvas>
    <script>
    (function() {
        var canvas = document.getElementById('stardust-canvas');
        if (!canvas) return;
        var ctx = canvas.getContext('2d');
        var stars = [];
        var count = 100;
        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resize);
        resize();
        var colors = ['rgba(230, 237, 243, 0.7)', 'rgba(88, 166, 255, 0.7)', 'rgba(227, 179, 65, 0.7)'];
        for (var i = 0; i < count; i++) {
            var r = Math.random() * 2 + 0.5;
            var depth = r / 2.5;
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                r: r,
                color: colors[Math.floor(Math.random() * colors.length)],
                vy: (Math.random() * 0.4 + 0.1) * depth,
                vx: (Math.random() * 0.2 - 0.1) * depth
            });
        }
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (var i = 0; i < count; i++) {
                var s = stars[i];
                var grad = ctx.createRadialGradient(s.x, s.y, 0, s.x, s.y, s.r * 2);
                grad.addColorStop(0, s.color);
                grad.addColorStop(1, 'rgba(13, 17, 23, 0)');
                ctx.fillStyle = grad;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r * 2, 0, Math.PI * 2, true);
                ctx.fill();
                s.y -= s.vy;
                s.x += s.vx;
                if (s.y < 0) {
                    s.y = canvas.height;
                    s.x = Math.random() * canvas.width;
                }
                if (s.x < 0 || s.x > canvas.width) {
                    s.vx = -s.vx;
                }
            }
            requestAnimationFrame(draw);
        }
        draw();
    })();
    </script>
    """, unsafe_allow_html=True)
