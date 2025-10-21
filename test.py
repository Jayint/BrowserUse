from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv
import asyncio

load_dotenv()

browser = Browser(
    # 使用 Playwright 的 Chromium，更稳定
    # executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
)

task = """
    1.访问https://quotes.toscrape.com/
    2.使用提取操作，查询 “前 3 条名言及其作者”
    3.使用写入文件操作将结果保存到 quotes.csv 中
    4.在谷歌上搜索第一条名言，查找其创作时间"
"""
llm = ChatGoogle(model="gemini-flash-latest")
agent = Agent(task=task, llm=llm, browser=browser)

async def main():
    await agent.run()

    input("按 Enter 关闭浏览器")
    
    await browser.close()
    
if __name__ == "__main__":
    asyncio.run(main())