from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from backend.models.base import Base
from sqlalchemy.orm import sessionmaker
import csv

class NewAndReturningViewersChartData(Base):
    __tablename__ = 'new_returning_viewers_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    New_Returning_Viewers = Column(String)
    Views = Column(Integer)

class NewAndReturningViewersTableData(Base):
    __tablename__ = 'new_returning_viewers_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    New_Returning_Viewers = Column(String)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class NewAndReturningViewersTotals(Base):
    __tablename__ = 'new_returning_viewers_totals'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Views = Column(Integer)

