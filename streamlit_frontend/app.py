import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="GPT-4o × MCPデモ", layout="wide")
st.title("🧠 GPT-4oがMCPツール（FastAPI）を使うデモ")

if "OPENAI_API_KEY" not in st.secrets:
    st.error("OPENAI_API_KEY が設定されていません。")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

MCP_OPENAPI_URL = "https://your-fastapi-name.onrender.com/openapi.json"

user_input = st.text_input("GPTに渡すメッセージを入力してください")

if st.button("送信してMCPツールを呼び出す"):
    with st.spinner("GPT-4oがFastAPI MCPツールを呼び出しています..."):
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {"role": "user", "content": f"次のメッセージをMCPツールでエコーして: {user_input}"}
            ],
            tool_choice="auto",
            tools=[
                {
                    "type": "openapi",
                    "spec": {
                        "url": MCP_OPENAPI_URL
                    }
                }
            ]
        )
        reply = response.choices[0].message.content
        st.success("✅ GPTからの応答:")
        st.write(reply)
