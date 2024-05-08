from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class GeographyChartData(Base):
    __tablename__ = 'geography_chart_data'

    Date = Column(Date, primary_key=True)
    Geography = Column(String, primary_key=True)
    Views = Column(Integer)

class GeographyTableData(Base):
    __tablename__ = 'geography_table_data'

    Date = Column(Date, primary_key=True)
    Geography = Column(String, primary_key=True)
    Views = Column(Integer)

class GeographyTotals(Base):
    __tablename__ = 'geography_totals'

    Date = Column(Date, primary_key=True)
    Geography = Column(String, primary_key=True)
    Views = Column(Integer)

