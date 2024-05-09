from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.orm import sessionmaker

import sys
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)

# Add the grandparent directory to the system path
sys.path.insert(0, grandparent_dir)

from backend.models.base import Base


class CitiesChartData(Base):
    __tablename__ = 'cities_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, primary_key=True)
    Cities = Column(String, primary_key=True)
    CityName = Column(String)
    Views = Column(Integer)

class CitiesTableData(Base):
    __tablename__ = 'cities_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Cities = Column(String, primary_key=True)
    CityName = Column(String)
    Geography1 = Column(String)
    Geography2 = Column(String)
    Views = Column(Integer)
    WatchTime = Column(Float)
    AverageViewDuration = Column(Time)

class CitiesTotals(Base):
    __tablename__ = 'cities_totals'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, primary_key=True)
    Views = Column(Integer)
