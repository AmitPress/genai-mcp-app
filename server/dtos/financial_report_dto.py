from dataclasses import dataclass
from typing import Optional

@dataclass
class FinancialReportDTO:
    company_name: str
    year: int
    period: int 

    income_statement: Optional[int] = None
    balance_sheet: Optional[int] = None
    cashflow_statement: Optional[int] = None
    equity_statement: Optional[int] = None


@dataclass
class IncomeStatementDTO:
    financial_report_id: Optional[int] = None
    revenue: float = 0
    cost_of_goods_sold: float = 0
    gross_profit: float = 0
    net_income: float = 0


@dataclass
class BalanceSheetDTO:
    financial_report_id: Optional[int] = None
    assets: float = 0
    liabilities: float = 0
    equity: float = 0


@dataclass
class CashFlowStatementDTO:
    financial_report_id: Optional[int] = None
    operating_activities: float = 0
    investing_activities: float = 0
    financing_activities: float = 0
    net_cash_flow: float = 0


@dataclass
class EquityStatementDTO:
    financial_report_id: Optional[int] = None
    beginning_equity: float = 0
    net_income: float = 0
    dividends: float = 0
    ending_equity: float = 0