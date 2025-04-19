from db_conn import session, FinancialReport, BalanceSheet, IncomeStatement, EquityStatement, CashFlowStatement
from dtos.financial_report_dto import FinancialReportDTO, BalanceSheetDTO, IncomeStatementDTO, EquityStatementDTO, CashFlowStatementDTO
""" The Parameters must contain company name, year and period """

""" Create A Financial Report """
def create_report(fr_dto: FinancialReportDTO):
    fr = FinancialReport()
    fr.company_name = fr_dto.company_name
    fr.year = fr_dto.year 
    fr.period = fr_dto.period

    fr.balance_sheet = fr_dto.balance_sheet
    fr.income_statement = fr_dto.income_statement
    fr.cashflow_statement = fr_dto.cashflow_statement
    fr.equity_statement = fr_dto.equity_statement

    session.add(fr)
    session.commit()
    return fr

""" Get Financial Report """
def find_report(company, year, period):
    result = session.query(FinancialReport).filter(FinancialReport.company_name == company, FinancialReport.year == year, FinancialReport.period == period).first()
    return result


""" Create Balance Sheet """
def create_balance_sheet(bs_dto: BalanceSheetDTO):
    bs = BalanceSheet()
    bs.assets = bs_dto.assets
    bs.liabilities = bs_dto.liabilities
    bs.equity = bs_dto.equity
    bs.financial_report_id = bs_dto.financial_report_id

    session.add(bs)
    session.commit()
    return bs

""" Get Balance Sheet """
def find_balance_sheet(balance_sheet_id):
    results = session.query(BalanceSheet).filter(BalanceSheet.id == balance_sheet_id)
    return results

""" Create Income Statement """
def create_income_statement(is_dto: IncomeStatementDTO):
    ins = IncomeStatement()
    ins.revenue = is_dto.revenue
    ins.cost_of_goods_sold = is_dto.cost_of_goods_sold
    ins.gross_profit = is_dto.gross_profit
    ins.net_income = is_dto.net_income
    ins.financial_report_id = is_dto.financial_report_id

    session.add(ins)
    session.commit()
    return ins

""" Get Income Statement """
def find_income_statement(income_statement_id):
    results = session.query(IncomeStatement).filter(IncomeStatement.id == income_statement_id)
    return results

""" Create Equity Statement """
def create_equity_statement(es_dto: EquityStatementDTO):
    es = EquityStatement()
    es.beginning_equity = es_dto.beginning_equity    
    es.net_income = es_dto.net_income
    es.dividends = es_dto.dividends
    es.ending_equity = es_dto.ending_equity
    es.financial_report_id = es_dto.financial_report_id

    session.add(es)    
    session.commit()
    return es

""" Get Equity Statement """
def find_equity_statement(equity_statement_id):
    results = session.query(EquityStatement).filter(EquityStatement.id == equity_statement_id)
    return results

""" Create Cash Flow Statement """
def create_cashflow_statement(cs_dto: CashFlowStatementDTO):    
    cs = CashFlowStatement()
    cs.operating_activities = cs_dto.operating_activities    
    cs.investing_activities = cs_dto.investing_activities
    cs.financing_activities = cs_dto.financing_activities
    cs.net_cash_flow = cs_dto.net_cash_flow
    cs.financial_report_id = cs_dto.financial_report_id

    session.add(cs)    
    session.commit()
    return cs

""" Get Cash Flow Statement """
def find_cashflow_statement(cashflow_statement_id):
    results = session.query(CashFlowStatement).filter(CashFlowStatement.id == cashflow_statement_id)
    return results