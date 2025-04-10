# AI 自动出题助手 (DeepSeek + Streamlit)

一个使用 DeepSeek API 实现的自动题目生成工具，基于 Streamlit 部署。

## 本地运行
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud 部署
1. 上传本项目到 GitHub
2. 在 `.streamlit/secrets.toml` 中配置 API 密钥：
```
DEEPSEEK_API_KEY = "你的密钥"
```
3. 到 https://streamlit.io/cloud 部署