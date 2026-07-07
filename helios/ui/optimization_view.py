import streamlit as st

from models.registry import MODEL_REGISTRY


def render_model_cards(results):

    st.markdown(
        "## 🤖 Model Intelligence Arena"
    )

    cols = st.columns(3)

    for index, (model, meta) in enumerate(
        MODEL_REGISTRY.items()
    ):

        with cols[index % 3]:

            model_type = meta.get(
                "type",
                "unknown"
            )

            st.markdown(
                f"""
                ### {model}

                Provider:
                {meta.get('provider','unknown')}

                Type:
                {model_type}

                Quality:
                {meta.get('quality',0)}

                Cost:
                {meta.get('cost',0)}

                Latency:
                {meta.get('latency',0)}
                """
            )
