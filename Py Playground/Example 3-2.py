from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base #This you have to declare your own schemas like NoSQL and MongoDB
Base = declarative_base()


class winnerTable(Base): #a child class of Base object
    __tablename__ = 'winner'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationaliy = Column(String)
    sex = Column(Enum('male','female'))

    def __repr__(self):
        return "a string of crap"

Base.metadata.create_all(engine)
