import streamlit as st

st.logo(
    "assets/echo_logo_light.png",
    size="large",
    link=None,
    icon_image="assets/logo.png",
)

st.title("📄 Document Upload")
st.caption("⬆️ Upload your documents for analysis")

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    st.subheader("📄 File Information")
    st.write(f"**Name:** {uploaded_file.name}")
    st.write(f"**Type:** {uploaded_file.type}")
    st.write(f"**Size:** {uploaded_file.size} bytes")

    if uploaded_file.type == "text/plain":
        st.subheader("📜 File Content")
        content = uploaded_file.read().decode("utf-8")
        st.text(content)

    st.success("✅ Upload successful!")
else:
    st.info("Please upload a file to continue.")
