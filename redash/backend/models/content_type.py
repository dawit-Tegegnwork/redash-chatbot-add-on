from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from backend.models.base import Base
from sqlalchemy.orm import sessionmaker
import csv


class ContentTypeChartData(Base):
    __tablename__ = 'content_type_chart_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Content_Type = Column(String)
    Views = Column(Integer)

class ContentTypeTableData(Base):
    __tablename__ = 'content_type_table_data'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Content_Type = Column(String)
    Views = Column(Integer)
    Watch_Time = Column(Float)
    Average_View_Duration = Column(Time)

class ContentTypeTotals(Base):
    __tablename__ = 'content_type_totals'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Views = Column(Integer)

# # Define your database connection
# engine = create_engine('sqlite:///content_type_data.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Read and insert data from CSV files
# csv_files = {
#     'ContentTypeChartData.csv': ContentTypeChartData,
#     'ContentTypeTableData.csv': ContentTypeTableData,
#     'ContentTypeTotals.csv': ContentTypeTotals
# }

# for file, model in csv_files.items():
#     with open(file, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             session.add(model(**row))

# session.commit()
