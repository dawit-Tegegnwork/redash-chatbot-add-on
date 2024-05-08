from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class DeviceTypeChartData(Base):
    __tablename__ = 'device_type_chart_data'

    Date = Column(Date, primary_key=True)
    Device_Type = Column(String, primary_key=True)
    Views = Column(Integer)

class DeviceTypeTableData(Base):
    __tablename__ = 'device_type_table_data'

    Device_Type = Column(String, primary_key=True)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class DeviceTypeTotals(Base):
    __tablename__ = 'device_type_totals'

    Date = Column(Date, primary_key=True)
    Views = Column(Integer)

