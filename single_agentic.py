from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()
#NEWS AGENT

news_agent = Agent(
    name = "News Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = [
        'search the latest financial news about Nvidia stocks',
        'search the top 5 news articles',
        'provide key insights in markdown format for read',
        'search the Data scince and Data Analytic jobs operchunities'
        ],
        show_tool_calls=True,
        markdown=True,
        debug_mode=True
)

news_agent.print_response(
    "Find the summarized latest financial news about Nvidia stocks",
    stream= True
)