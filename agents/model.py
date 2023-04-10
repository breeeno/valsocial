from sqlalchemy import Column, Integer, String
from settings import Base


class Agents(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    external_id = Column(String, unique=True, nullable=False)
    role = Column(String, unique=False, nullable=False)
    ability_1_name = Column(String, unique=True, nullable=False)
    ability_1_description = Column(String, unique=True, nullable=False)
    ability_2_name = Column(String, unique=True, nullable=False)
    ability_2_description = Column(String, unique=True, nullable=False)
    ability_3_name = Column(String, unique=True, nullable=False)
    ability_3_description = Column(String, unique=True, nullable=False)
    ability_4_name = Column(String, unique=True, nullable=False)
    ability_4_description = Column(String, unique=True, nullable=False)
    ability_5_name = Column(String, unique=False, nullable=True)
    ability_5_description = Column(String, unique=False, nullable=True)
