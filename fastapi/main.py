from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import date
from collections import defaultdict
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from database import Base,engine,SessionLocal

class ExpenseDB(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)

Base.metadata.create_all(bind=engine)

# -------------------------------
# Pydantic Schemas
# -------------------------------
class Expense(BaseModel):
    title: str
    amount: float
    category: str
    date: date

# class ExpenseOut(Expense):
#     id: int
#     class Config:
#         orm_mode = True

# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(title="Expense Tracker with DB")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# CRUD Endpoints
# -------------------------------
@app.post("/expenses/", response_model=ExpenseOut)
def add_expense(expense: Expense, db: Session = Depends(get_db)):
    new_expense = ExpenseDB(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.get("/expenses/", response_model=List[ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return db.query(ExpenseDB).all()

@app.get("/expenses/{expense_id}", response_model=ExpenseOut)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    return exp

@app.put("/expenses/{expense_id}", response_model=ExpenseOut)
def update_expense(expense_id: int, updated: Expense, db: Session = Depends(get_db)):
    exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    for key, value in updated.dict().items():
        setattr(exp, key, value)

    db.commit()
    db.refresh(exp)
    return exp

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    db.delete(exp)
    db.commit()
    return {"message": "Expense deleted"}

# -------------------------------
# Summary Endpoints
# -------------------------------
@app.get("/summary/category")
def summarize_by_category(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseDB).all()
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount
    return summary

@app.get("/summary/month")
def summarize_by_month(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseDB).all()
    summary = defaultdict(float)
    for exp in expenses:
        key = exp.date.strftime("%Y-%m")  # YYYY-MM
        summary[key] += exp.amount
    return summary

# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine, Base
# import models

# # Create tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def read_root():
#     return {"message": "FastAPI is running and connected to DB!"}


# # steps to install fast FastAPI

# # 1) python -m venv venv

# # 2) .\venv\Scripts\Activate.ps1

# # 3) python -m pip install --upgrade pip

# # 4) pip install fastapi uvicron

# # 5)uvicron main:app --reload