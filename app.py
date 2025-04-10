import streamlit as st
import openai

# ✅ DeepSeek 新版 API 地址和密钥
openai.api_base = "https://api.deepseek.com"
openai.api_key = st.secrets.get("DEEPSEEK_API_KEY")

def build_prompt(subject, topic, qtype):
    return f"""
    请根据以下信息生成一道题目并附上答案：
    学科：{subject}
    知识点：{topic}
    题型：{qtype}
    要求：题干简洁，选项合理（如适用），附正确答案与简要解析。
    """

def generate_question(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",  # ✅ 使用最新模型名
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"生成失败: {e}"

st.set_page_config(page_title="AI 出题助手", layout="centered")
st.title("🧠 AI 自动出题助手 (DeepSeek)")
st.write("输入知识点，AI 自动生成题目与解析 ✍️")

subject = st.selectbox("选择学科：", ["数学", "语文", "英语", "物理", "化学"])
topic = st.text_input("请输入知识点：", "勾股定理")
qtype = st.selectbox("选择题型：", ["选择题", "填空题", "简答题"])

if st.button("🎯 生成题目"):
    with st.spinner("AI 出题中..."):
        prompt = build_prompt(subject, topic, qtype)
        result = generate_question(prompt)
        st.markdown("---")
        st.markdown(f"#### 🎓 生成结果：\n\n{result}")
