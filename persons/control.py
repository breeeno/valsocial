from fastapi import HTTPException
from passlib.context import CryptContext

from agents.model import Agents
from persons.model import Person
from settings import Session

elos = ['UNRANKED', 'IRON_1', 'IRON_2', 'IRON_3', 'BRONZE_1', 'BRONZE_2', 'BRONZE_3', 'SILVER_1', 'SILVER_2',
        'SILVER_3', 'GOLD_1', 'GOLD_2', 'GOLD_3', 'PLATINUM_1', 'PLATINUM_2', 'PLATINUM_3', 'DIAMOND_1', 'DIAMOND_2',
        'DIAMOND_3', 'ASCENDENT_1', 'ASCENDENT_2', 'ASCENDENT_3', 'IMMORTAL_1', 'IMMORTAL_2', 'IMMORTAL_3', 'RADIANT']

session = Session()
hash_password = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_agent_id(agent_id):
    agents_ids = []
    agent_query = session.query(Agents).all()
    for agent_obj in agent_query:
        agents_ids.append(str(agent_obj.id))
    if agent_id not in agents_ids:
        return HTTPException(status_code=400, detail="agent_id doesn't match any agent.")
    return agent_id


def verify_elo(elo):
    if elo not in elos:
        return HTTPException(status_code=400, detail="person elo doesn't match any existent elo.")
    return elo


def get_password_hash(password):
    return hash_password.hash(password)


class PersonController:
    name: str
    person_id: str
    password: str
    elo: str
    favorite_agent_id: str
    is_private: bool
    email: str

    def __init__(self, name: str = None, person_id: str = None, password: str = None, elo: str = None, favorite_agent_id: str = None,
                 is_private: bool = None, email: str = None):
        self.name = name
        self.person_id = person_id
        self.password = password
        self.elo = elo
        self.favorite_agent_id = favorite_agent_id
        self.is_private = is_private
        self.email = email

    def create_new_person(self):
        sucess_msg = {'message': 'Register concluded.'}
        verify_email = session.query(Person).filter_by(email=self.email).first()
        if verify_email:
            return HTTPException(status_code=400, detail='Email already existent.')
        person = Person(name=self.name,
                        email=self.email,
                        password=get_password_hash(self.password),
                        elo=verify_elo(self.elo),
                        favorite_agent_id=verify_agent_id(self.favorite_agent_id),
                        is_private=self.is_private)
        session.add(person)
        session.commit()
        return sucess_msg

