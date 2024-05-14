from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from backend.models.base import Base
from sqlalchemy.orm import sessionmaker
import csv


class DeviceTypeChartData(Base):
    __tablename__ = 'device_type_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Device_Type = Column(String)
    Views = Column(Integer)

class DeviceTypeTableData(Base):
    __tablename__ = 'device_type_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Device_Type = Column(String)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class DeviceTypeTotals(Base):
    __tablename__ = 'device_type_totals'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Views = Column(Integer)

