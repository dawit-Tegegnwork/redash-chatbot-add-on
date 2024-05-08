from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class NewAndReturningViewersChartData(Base):
    __tablename__ = 'new_returning_viewers_chart_data'

    Date = Column(Date, primary_key=True)
    New_Returning_Viewers = Column(String, primary_key=True)
    Views = Column(Integer)

class NewAndReturningViewersTableData(Base):
    __tablename__ = 'new_returning_viewers_table_data'

    New_Returning_Viewers = Column(String, primary_key=True)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class NewAndReturningViewersTotals(Base):
    __tablename__ = 'new_returning_viewers_totals'

    Date = Column(Date, primary_key=True)
    Views = Column(Integer)

