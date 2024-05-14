from sqlalchemy import create_engine, Column, Integer, String, Date
from backend.models.base import Base
from sqlalchemy.orm import sessionmaker
import csv

class GeographyChartData(Base):
    __tablename__ = 'geography_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Geography = Column(String)
    Views = Column(Integer)

class GeographyTableData(Base):
    __tablename__ = 'geography_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Geography = Column(String)
    Views = Column(Integer)

class GeographyTotals(Base):
    __tablename__ = 'geography_totals'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Geography = Column(String)
    Views = Column(Integer)

