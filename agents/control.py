import requests
from fastapi import HTTPException
from agents.model import Agents
from settings import Session

session = Session()


class AgentsController:
    id_agent: int

    def __init__(self, id_agent: int = None):
        self.id_agent = id_agent

    @staticmethod
    def get_or_update_agents():
        params = {
            'isPlayableCharacter': True
        }
        response = requests.get('https://valorant-api.com/v1/agents', params=params)
        data = response.json()
        output = []
        for agent in data["data"]:
            abilities = agent["abilities"]
            habilities_dict = {}
            for i in range(5):
                if i < len(abilities):
                    habilities_dict[f"ability_{i + 1}_name"] = abilities[i]["displayName"]
                    habilities_dict[f"ability_{i + 1}_description"] = abilities[i]["description"]
                else:
                    habilities_dict[f"ability_{i + 1}_name"] = ""
                    habilities_dict[f"ability_{i + 1}_description"] = ""

            output.append({
                "agent_name": agent["displayName"],
                "external_id": agent["uuid"],
                "description": agent["description"],
                "role": agent["role"]["displayName"],
                **habilities_dict
            })
        return output

    def get_one_agent(self):
        agent_query = session.query(Agents).filter_by(id=self.id_agent).first()
        if agent_query is None:
            raise HTTPException(status_code=404, detail="Agent not found")
        response = {"name": agent_query.name,
                    "role": agent_query.role,
                    "ability_1_name": agent_query.ability_1_name,
                    "ability_1_description": agent_query.ability_1_description,
                    "ability_2_name": agent_query.ability_2_name,
                    "ability_2_description": agent_query.ability_2_description,
                    "ability_3_name": agent_query.ability_3_name,
                    "ability_3_description": agent_query.ability_3_description,
                    "ability_4_name": agent_query.ability_4_name,
                    "ability_4_description": agent_query.ability_4_description,
                    "ability_5_name": agent_query.ability_5_name,
                    "ability_5_description": agent_query.ability_5_description,
                    }
        return response

    @staticmethod
    def get_all_agents():
        agent_query = session.query(Agents).all()
        agents_list = []
        for agent_obj in agent_query:
            obj = {"name": agent_obj.name,
                   "role": agent_obj.role,
                   "ability_1_name": agent_obj.ability_1_name,
                   "ability_1_description": agent_obj.ability_1_description,
                   "ability_2_name": agent_obj.ability_2_name,
                   "ability_2_description": agent_obj.ability_2_description,
                   "ability_3_name": agent_obj.ability_3_name,
                   "ability_3_description": agent_obj.ability_3_description,
                   "ability_4_name": agent_obj.ability_4_name,
                   "ability_4_description": agent_obj.ability_4_description,
                   "ability_5_name": agent_obj.ability_5_name,
                   "ability_5_description": agent_obj.ability_5_description,
                   }
            agents_list.append(obj)
        response = {'agents': agents_list}
        return response
