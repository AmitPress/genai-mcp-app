from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey

# create tables
Base = declarative_base()

# tables here

class FinancialReport(Base):
    __tablename__ = 'financial_reports'

    PERIOD_CHOICES = (
        ("annually", "Annually"),
        ("quarterly", "Quarterly"),
        ("monthly", "Monthly"),
    )

    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    period = Column(String, default="Annually")

    income_statement = relationship("IncomeStatement", uselist=False, back_populates="report")
    balance_sheet = relationship("BalanceSheet", uselist=False, back_populates="report")
    cashflow_statement = relationship("CashFlowStatement", uselist=False, back_populates="report")
    equity_statement = relationship("EquityStatement", uselist=False, back_populates="report")



class IncomeStatement(Base):
    __tablename__ = 'income_statements'

    id = Column(Integer, primary_key=True)
    financial_report_id = Column(Integer, ForeignKey('financial_reports.id'))
    revenue = Column(Float)
    cost_of_goods_sold = Column(Float)
    gross_profit = Column(Float)
    net_income = Column(Float)

    report = relationship("FinancialReport", back_populates="income_statement")

class BalanceSheet(Base):
    __tablename__ = 'balance_sheets'

    id = Column(Integer, primary_key=True)
    financial_report_id = Column(Integer, ForeignKey('financial_reports.id'))
    assets = Column(Float)
    liabilities = Column(Float)
    equity = Column(Float)

    report = relationship("FinancialReport", back_populates="balance_sheet")

class CashFlowStatement(Base):
    __tablename__ = 'cashflow_statements'

    id = Column(Integer, primary_key=True)
    financial_report_id = Column(Integer, ForeignKey('financial_reports.id'))
    operating_activities = Column(Float)
    investing_activities = Column(Float)
    financing_activities = Column(Float)
    net_cash_flow = Column(Float)

    report = relationship("FinancialReport", back_populates="cashflow_statement")

class EquityStatement(Base):
    __tablename__ = 'equity_statements'

    id = Column(Integer, primary_key=True)
    financial_report_id = Column(Integer, ForeignKey('financial_reports.id'))
    beginning_equity = Column(Float)
    net_income = Column(Float)
    dividends = Column(Float)
    ending_equity = Column(Float)

    report = relationship("FinancialReport", back_populates="equity_statement")


engine = create_engine('sqlite:///financial_statements.db', echo=True)

Base.metadata.create_all(engine)


# sessions

Session = sessionmaker(bind=engine)
session = Session()