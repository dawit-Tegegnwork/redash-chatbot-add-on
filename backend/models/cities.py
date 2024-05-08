from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CitiesChartData(Base):
    __tablename__ = 'cities_chart_data'

    Date = Column(Date, primary_key=True)
    Cities = Column(String, primary_key=True)
    CityName = Column(String)
    Views = Column(Integer)

class CitiesTableData(Base):
    __tablename__ = 'cities_table_data'

    Cities = Column(String, primary_key=True)
    CityName = Column(String, primary_key=True)
    Geography1 = Column(String)
    Geography2 = Column(String)
    Views = Column(Integer)
    WatchTime = Column(Float)
    AverageViewDuration = Column(Time)

class CitiesTotals(Base):
    __tablename__ = 'cities_totals'

    Date = Column(Date, primary_key=True)
    Views = Column(Integer)
