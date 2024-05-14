from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from backend.models.base import Base
from sqlalchemy.orm import sessionmaker
import csv


class OperatingSystemChartData(Base):
    __tablename__ = 'operating_system_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Operating_System = Column(String)
    Views = Column(Integer)

class OperatingSystemTableData(Base):
    __tablename__ = 'operating_system_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Operating_System = Column(String)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class OperatingSystemTotals(Base):
    __tablename__ = 'operating_system_totals'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Views = Column(Integer)
