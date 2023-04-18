from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import ChoiceType
from agents.model import Agents
from settings import Base

ELOS_CHOICES = [('UNRANKED', 'UNRANKED'), ('IRON 1', 'IRON 1'), ('IRON 2', 'IRON 2'), ('IRON 3', 'IRON 3'),
                ('BRONZE 1', 'BRONZE 1'), ('BRONZE 2', 'BRONZE 2'), ('BRONZE 3', 'BRONZE 3'), ('SILVER 1', 'SILVER 1'),
                ('SILVER 2', 'SILVER 2'), ('SILVER 3', 'SILVER 3'), ('GOLD 1', 'GOLD 1'), ('GOLD 2', 'GOLD 2'),
                ('GOLD 3', 'GOLD 3'), ('PLATINUM 1', 'PLATINUM 1'), ('PLATINUM 2', 'PLATINUM 2'),
                ('PLATINUM 3', 'PLATINUM 3'), ('DIAMOND 1', 'DIAMOND 1'), ('DIAMOND 2', 'DIAMOND 2'),
                ('DIAMOND 3', 'DIAMOND 3'), ('ASCENDENT_1', 'ASCENDENT_1'), ('ASCENDENT_2', 'ASCENDENT_2'),
                ('ASCENDENT_3', 'ASCENDENT_3'), ('IMMORTAL_1', 'IMMORTAL_1'), ('IMMORTAL_2', 'IMMORTAL_2'),
                ('IMMORTAL_3', 'IMMORTAL_3'), ('RADIANT', 'RADIANT')]


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=False, nullable=False)
    password = Column(String, nullable=False)
    elo = Column(ChoiceType(ELOS_CHOICES), default='UNRANKED', nullable=False)
    favorite_agent_id = Column(Integer, ForeignKey('agents.id'))
    favorite_agent = relationship(Agents, backref=backref('person', uselist=True))
    is_private = Column(Boolean, default=False)


class PersonFriends(Base):
    __tablename__ = "person_friends"
    id = Column(Integer, primary_key=True)
    person_1_id = Column(Integer, ForeignKey('person.id'))
    person_1 = relationship("Person", foreign_keys=[person_1_id])
    person_2_id = Column(Integer, ForeignKey('person.id'))
    person_2 = relationship("Person", foreign_keys=[person_2_id])
