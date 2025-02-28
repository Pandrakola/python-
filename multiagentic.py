from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import streamlit as str
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#LIVE CRICKET AGENT

match_agent = Agent(
    name = "Live match agent",
    model = OpenAIChat(id="gpt-4o",api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=[
        'search for live cricket match score',
        'summerize the score, top players, and match sitchuvations ',
        'use markdown table for the batter clarity and readabulity'
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

#2nd Agent player

player_agent = Agent(
    name = "player stats agent",
    model = OpenAIChat(id="gpt-4o",api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=[
        'find recent player statistics',
        'including batting and bowling last 5 matches',
        'use the table batter clarity and readdabulity'
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)


#3rd agent--Criket news Agent

news_agent = Agent(
    name = 'cricket news Agent',
    model = OpenAIChat(id="gpt-4o",api_key=api_key),
    tools=[DuckDuckGo],
    instructions=[
        'find and summerize the latest crecket news',
        'Higligts upcomin match,tournements,and player updates'  
        'List of headlines and key insite in markdown table for the batter clarity and readabulity,'
            ],
            show_tool_calls=True,
            markdown=True,
            debug_mode=True,

)

#main cricket news (combine all three agens)
cricket_team = Agent(
    name ="Cricket Analysis Team", 
    model = OpenAIChat(id='gpt-4o',api_key=api_key),
    tools = [DuckDuckGo],
    instructions=[
        'provide live cricket match score,playerstatistics and new update and summary',
        'user stucted markdown formate for better readabulaty and clarity'

    ],
    show_tool_calls=True,
            markdown=True,
            debug_mode=True,
)

cricket_team.print_response(
    "get the latest score of india vs pakistan match,recent stats for virat kohli and cricket news",
    stream = True,
)




#streamlit  UI
str.set_page_config(page_title = "LIVE UPDATES",layout="wide")
str.title("CRICKET AGENTIC AI _ SCORE, PLAYER STATS, NEWS")

col1,col2 =str.columns(2)
with col1:
    match_query = str.text_input("Enter match query","India vs pakistan live score")
with col2:
    player_query =str.text_input("Enter player","virat kohli recent stats")

    if str.button("Get cricket updates"):
        query = "Get the latest score"
        if match_query:
            query += f"of{match_query}"
            if player_query:
                query += f",recent stats for {player_query}"
                query += ",and latest cricket news"

                with str.spinner("feching cricket updates...."):
                    response = cricket_team.run(query)
                    str.markdown(response)
                    
                   