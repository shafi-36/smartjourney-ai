import streamlit as st
from agents.planner import run_agent

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner")
st.caption("Plan trips using natural language")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
query = st.chat_input(
    "Example: 2 day trip from MAA to CJB and Ooty under 15k"
)

if query:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    try:

        result = run_agent(query)

        with st.chat_message("assistant"):
           st.markdown(result)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": str(result)
            }
        )

    except Exception as e:

        with st.chat_message("assistant"):
            st.error(f"Error: {e}")