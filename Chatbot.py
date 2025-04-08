import time
import streamlit as st

def stream_data(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.04)

def generate_agent_responses():
    conversation = [
        {"name": "PolicyMakerAgent", "avatar": "🏛️", "role": "policy expert", "content": "We need to address the housing crisis with more effective policies. I suggest implementing mixed-income housing projects and adjusting rent control regulations to create a more balanced market."},
        {"name": "UrbanPlannerAgent", "avatar": "🏗️", "role": "urban planner", "content": "I agree. Additionally, I recommend vertical expansion and smart zoning laws to maximize land use efficiency while ensuring sustainable urban growth."},
        {"name": "InvestorAgent", "avatar": "💰", "role": "investment strategist", "content": "For these initiatives to succeed, we need financial incentives. Offering tax breaks to developers investing in underutilized areas could encourage more affordable housing projects."},
        {"name": "CommunityEngagementAgent", "avatar": "🏡", "role": "community engagement specialist", "content": "Based on feedback from residents, there is strong support for cooperative housing models and increased green spaces. If we want sustainable solutions, we must incorporate community input."},
        {"name": "PolicyMakerAgent", "avatar": "🏛️", "role": "policy expert", "content": "If cooperative housing is a popular option, we should integrate it into our policy frameworks by providing subsidies and creating legal structures that support these projects."},
        {"name": "InvestorAgent", "avatar": "💰", "role": "investment strategist", "content": "Cooperative housing could be financially viable if we introduce co-investment models where public and private sectors share the risks and returns."},
        {"name": "UrbanPlannerAgent", "avatar": "🏗️", "role": "urban planner", "content": "We can also designate specific zones for cooperative housing developments to ensure a structured and well-planned expansion."},
        {"name": "CommunityEngagementAgent", "avatar": "🏡", "role": "community engagement specialist", "content": "I will conduct further surveys to assess the feasibility and scalability of these solutions, ensuring they align with residents' needs and expectations."},
        {"name": "CommunityEngagementAgent", "avatar": "🏡", "role": "community engagement specialist", "content": "To make the research effective, I suggest structuring the survey as follows:\n\n1. **Demographic Information:** Age, household size, income range, occupation.\n2. **Current Housing Situation:** Do you rent or own your home? How much of your income is spent on housing? What are the biggest challenges you face regarding housing?\n3. **Housing Preferences:** Would you be interested in cooperative housing models? How important are green spaces in your neighborhood? Would you support mixed-income housing developments?\n4. **Urban Development Opinions:** Are you in favor of vertical expansion (high-rise buildings) to increase housing supply? What amenities do you consider essential in new housing developments? Would you support rezoning to allow for more housing units in your area?\n5. **Investment and Policy Input:** Should governments offer tax incentives to encourage affordable housing development? How do you feel about rent control policies? What other solutions do you think could help address the housing crisis?"},
        {"name": "PolicyMakerAgent", "avatar": "🏛️", "role": "policy expert", "content": "Once the survey results are gathered, we can refine our policies to better reflect public needs."},
        {"name": "UrbanPlannerAgent", "avatar": "🏗️", "role": "urban planner", "content": "And ensure urban development aligns with both sustainability goals and community expectations."},
        {"name": "InvestorAgent", "avatar": "💰", "role": "investment strategist", "content": "With clear data, we can also create better incentives for developers to support affordable and inclusive housing projects."},
        {"name": "CommunityEngagementAgent", "avatar": "🏡", "role": "community engagement specialist", "content": "Great! I’ll start working on collecting responses so we can move forward with an informed plan."},
    ]    

    responses = []
    for message in conversation:
        response_text = f"{message['name']} ({message['role']}): {message['content']}"
        responses.append({"role": "assistant", "avatar": message["avatar"], "content": response_text})  

    return responses

st.set_page_config(layout="wide")

st.logo(
    "assets/echo_logo_light.png",
    size="large",
    link=None,
    icon_image="assets/logo.png",
)

st.markdown(
    """
    <style>  

    div[data-testid="stHorizontalBlock"] > div {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
    }

    textarea {
        background-color: #fff !important;
    }    

    [data-testid="stFileUploaderDropzone"] {
        background-color: #fff !important;
        padding: 10px !important;
        border-radius: 8px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

if "scenarios" not in st.session_state:
    st.session_state.scenarios = ["Scenario 1", "Scenario 2", "Scenario 3"]

if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = st.session_state.scenarios[0]

st.sidebar.title("Scenarios")

for scenario in st.session_state.scenarios:
    if st.sidebar.button(scenario, use_container_width=True):
        st.session_state.selected_scenario = scenario
        st.rerun()

if st.sidebar.button("➕ New scenario", use_container_width=True):
    new_scenario_name = f"Scenario {len(st.session_state.scenarios) + 1}"
    st.session_state.scenarios.append(new_scenario_name)
    st.session_state.selected_scenario = new_scenario_name
    st.rerun()

st.title(st.session_state.selected_scenario)
tabs = st.tabs(["Scenario design", "Results"])

with tabs[0]:
    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col1:
        st.subheader("Community representative")
        st.caption("Describe the type of community member you would like to hear from")

        if "representatives" not in st.session_state:
            st.session_state.representatives = [""]

        for i, rep in enumerate(st.session_state.representatives):
            st.session_state.representatives[i] = st.text_area(f"Representative {i+1}", rep, key=f"rep_{i}")

        if st.button("➕ Add another representative", use_container_width=True):
            st.session_state.representatives.append("")
            st.rerun()

    with col2:
        st.subheader("Document selection")
        st.caption("Select the documents you would like the scenario to take into account")
   
        if "uploaded_docs" not in st.session_state:
            st.session_state.uploaded_docs = []

        uploaded_files = st.file_uploader("Upload documents", accept_multiple_files=True)

      
    with col3:
        st.subheader("Questions")
        st.caption("Select the questions that you would like the scenario to ask")

        if "questions" not in st.session_state:
            st.session_state.questions = [""]

        for i, question in enumerate(st.session_state.questions):
            st.session_state.questions[i] = st.text_area(f"Question {i+1}", question, key=f"question_{i}")

        if st.button("➕ Add another question", use_container_width=True):
            st.session_state.questions.append("")
            st.rerun()

    st.markdown("---")
    if st.button("▶️ Run scenario", type="primary", ):
        st.success("Scenario executed! (mock)")

with tabs[1]:
    AGENTS = [
        {"name": "PolicyMakerAgent", "avatar": "🏛️", "role": "policy expert"},
        {"name": "UrbanPlannerAgent", "avatar": "🏗️", "role": "urban planner"},
        {"name": "InvestorAgent", "avatar": "💰", "role": "investment strategist"},
        {"name": "CommunityEngagementAgent", "avatar": "🏡", "role": "community engagement specialist"},
    ]

    USER_AVATAR = "👤"

    MULTI_AGENT_KEY_PREFIX = "multi_agent_"

    if f"{MULTI_AGENT_KEY_PREFIX}messages" not in st.session_state:
        st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"] = [{"role": "assistant", "content": "Hello! We are a team of agents. How can we assist you?"}]
        st.session_state[f"{MULTI_AGENT_KEY_PREFIX}responses_generated"] = False

    for msg in st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"]:
        with st.chat_message(msg["role"], avatar=msg.get("avatar", "🤖")):
            st.write(msg["content"])    

    if not st.session_state.get(f"{MULTI_AGENT_KEY_PREFIX}responses_generated", False):
        agent_responses = generate_agent_responses()
        for response in agent_responses:
            st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"].append(response)
            with st.chat_message("assistant", avatar=response["avatar"]):
                st.write_stream(stream_data(response["content"]))        
    
        st.session_state[f"{MULTI_AGENT_KEY_PREFIX}responses_generated"] = True
