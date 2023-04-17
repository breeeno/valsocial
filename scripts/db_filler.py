from agents.control import AgentsController
from agents.model import Agents
from persons.model import Person, PersonFriends
from settings import Base, engine, Session

session = Session()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    data = AgentsController.get_or_update_agents()
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
