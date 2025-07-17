from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Court(Base):
    __tablename__ = "courts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    city = Column(String, nullable=False)
    adaptive_support = Column(Boolean, default=False)
    booking_url = Column(String, nullable=True)


class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    court_id = Column(Integer, ForeignKey("courts.id"), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    is_available = Column(Boolean, default=True)


class ClickLog(Base):
    __tablename__ = "click_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=True)  # Optional
    court_id = Column(Integer, ForeignKey("courts.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
