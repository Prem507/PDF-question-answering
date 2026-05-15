import streamlit as st
import pdfplumber
from groq import Groq
import datetime
import io

st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI Chat Assistant")
st.caption("Chat with AI · Upload a PDF and ask questions about it")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input("Groq API Key", type="password", placeholder="Enter your Groq API key")

    st.divider()

    st.header("📄 Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        with st.spinner("Reading PDF..."):
            text_parts = []
            with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        text_parts.append(t)
            pdf_text = "\n".join(text_parts)

        if pdf_text.strip():
            st.session_state.pdf_text = pdf_text
            st.session_state.pdf_name = uploaded_file.name
            st.success(f"✅ PDF loaded: {uploaded_file.name}")
        else:
            st.error("Could not read text from this PDF.")

    if st.session_state.pdf_name:
        st.info(f"📑 Active PDF: **{st.session_state.pdf_name}**")
        if st.button("Remove PDF"):
            st.session_state.pdf_text = ""
            st.session_state.pdf_name = ""
            st.rerun()

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    if not api_key:
        st.warning("⚠️ Please enter your Groq API key in the sidebar.")
    else:
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Built-in shortcuts
        q = user_input.lower()
        if "time" in q:
            reply = f"The current time is {datetime.datetime.now().strftime('%H:%M')}."
        elif "your name" in q:
            reply = "I am your AI assistant!"
        elif "boss name" in q:
            reply = "Your boss is Premchandh."
        else:
            with st.spinner("Thinking..."):
                try:
                    client = Groq(api_key=api_key)

                    messages = [{"role": "system", "content": "You are a helpful AI assistant. Answer clearly and concisely."}]

                    if st.session_state.pdf_text:
                        messages.append({
                            "role": "user",
                            "content": (
                                f"Here is the content of the PDF '{st.session_state.pdf_name}':\n\n"
                                f"{st.session_state.pdf_text[:12000]}\n\n"
                                f"Now answer this question: {user_input}"
                            )
                        })
                    else:
                        for m in st.session_state.messages[:-1]:
                            messages.append({"role": m["role"], "content": m["content"]})
                        messages.append({"role": "user", "content": user_input})

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=messages
                    )
                    reply = response.choices[0].message.content

                except Exception as e:
                    reply = f"Error: {e}"

        with st.chat_message("assistant"):
            st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})