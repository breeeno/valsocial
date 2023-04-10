from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Enum as EnumType
from agents.model import Agents
from settings import Base


class Elos(Enum):
    IRON = 'IRON'
    BRONZE = 'BRONZE'
    SILVER = 'SILVER'
    GOLD = 'GOLD'
    PLATINUM = 'PLATINUM'
    DIAMOND = 'DIAMOND'
    ASCENDENT = 'ASCENDENT'
    IMMORTAL = 'IMMORTAL'
    RADIANT = 'RADIANT'
    UNRANKED = 'UNRANKED'


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    elo = Column(EnumType(Elos), default=Elos.UNRANKED, unique=False, nullable=False)
    favorite_agent_id = Column(Integer, ForeignKey('agents.id'))
    favorite_agent = relationship(Agents, backref=backref('person', uselist=True))
    is_private = Column(Boolean, default=False)


class PersonFriends(Base):
    __tablename__ = "person_friends"
    person_1_id = Column(Integer, ForeignKey('person.id'))
    person_1 = relationship(Person, backref=backref('person', uselist=True))
    person_2_id = Column(Integer, ForeignKey('person.id'))
    person_2 = relationship(Person, backref=backref('person', uselist=True))
