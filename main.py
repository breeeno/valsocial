from typing import Union

from fastapi import FastAPI

from agents.control import AgentsController

app = FastAPI()


@app.get("/agents/{agent_id}")
def get_individual_agent(agent_id: int):
    agent = AgentsController(agent_id)
    response = agent.get_one_agent()
    return response


@app.get("/agents")
def get_all_agents():
    agents = AgentsController()
    response = agents.get_all_agents()
    return response
