from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class OperatingSystemChartData(Base):
    __tablename__ = 'operating_system_chart_data'

    Date = Column(Date, primary_key=True)
    Operating_System = Column(String, primary_key=True)
    Views = Column(Integer)

class OperatingSystemTableData(Base):
    __tablename__ = 'operating_system_table_data'

    Operating_System = Column(String, primary_key=True)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class OperatingSystemTotals(Base):
    __tablename__ = 'operating_system_totals'

    Date = Column(Date, primary_key=True)
    Views = Column(Integer)
