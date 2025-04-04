import streamlit as st
import random
import time

st.logo(
    "assets/echo_logo_light.png",
    size="large",
    link=None,
    icon_image="assets/logo.png",
)

st.title("🤖 Multi-Agent AI Chat")
st.caption("💬 An example of a multi-agent chatbot")

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

for msg in st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"]:
    with st.chat_message(msg["role"], avatar=msg.get("avatar", "🤖")):
        st.write(msg["content"])
        

def generate_agent_responses(user_input):
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

def stream_data(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.04)

if prompt := st.chat_input("Type your question..."):
    st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"].append({"role": "user", "avatar": USER_AVATAR, "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.write(prompt)

    agent_responses = generate_agent_responses(prompt)
    for response in agent_responses:
        st.session_state[f"{MULTI_AGENT_KEY_PREFIX}messages"].append(response)
        with st.chat_message("assistant", avatar=response["avatar"]):
            st.write_stream(stream_data(response["content"]))
        # with st.spinner("Loading..."):
        #     time.sleep(2)
