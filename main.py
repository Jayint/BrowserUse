from browser_use import Agent, ChatGoogle
import openai
import os

# 加载环境变量
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化AI驱动的浏览器代理
agent = BrowserAgent(
    browser="chrome",  # 支持chrome/firefox/webkit
    headless=True,     # 无头模式
    ai_model="gpt-4o"  # 指定AI模型
)