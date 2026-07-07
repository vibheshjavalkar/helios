import streamlit as st


def render_mission_control(state):

    st.markdown(
        "## 🚀 HELIOS Mission Control"
    )

    tasks = state.get("tasks", [])
    logs = state.get("logs", [])
    results = state.get("results", [])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Tasks",
            len(tasks)
        )

    with col2:
        st.metric(
            "Models Available",
            6
        )

    with col3:
        st.metric(
            "System Status",
            "ACTIVE"
        )

    st.divider()

    st.markdown(
        "### Execution Pipeline"
    )

    for task in tasks:
        st.write(
            "🧠 " + task.get("name","Unknown")
        )

    st.divider()

    st.markdown(
        "### Runtime Logs"
    )

    for log in logs:
        st.write(
            "▶ " + str(log)
        )
