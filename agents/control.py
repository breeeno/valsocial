import requests
from agents.model import Agents
from settings import Base, engine, session


def busca_agentes():
    params = {
        'language': 'pt-BR',
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


if __name__ == '__main__':
    data = busca_agentes()
    Base.metadata.create_all(engine)
    for agent_data in data:
        agent = Agents(
            name=agent_data['agent_name'],
            external_id=agent_data['external_id'],
            role=agent_data['role'],
            ability_1_name=agent_data['ability_1_name'],
            ability_1_description=agent_data['ability_1_description'],
            ability_2_name=agent_data['ability_2_name'],
            ability_2_description=agent_data['ability_2_description'],
            ability_3_name=agent_data['ability_3_name'],
            ability_3_description=agent_data['ability_3_description'],
            ability_4_name=agent_data['ability_4_name'],
            ability_4_description=agent_data['ability_4_description'],
            ability_5_name=agent_data['ability_5_name'],
            ability_5_description=agent_data['ability_5_description'],
        )
        session.add(agent)
    session.commit()

