from datetime import datetime


from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(String, nullable=False)
    city = Column(String, nullable=False)
    connection_date = Column(DateTime, default=datetime.now, nullable=False)
    reports = relationship('WeatherReports', backref='report', lazy=True,cascade='all, delete-orphan')

    def __repr__(self):
        return self.tg_id

class WeatherReports(Base):
    __tablename__ = 'weatherReports'
    id = Column(Integer, primary_key=True)
    owner  = Column(Integer, ForeignKey('Users.id'), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
    temp = Column(Integer, nullable=False)
    feels_like = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    pressure_mm = Column(Integer, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return f'Из {self.city}'








