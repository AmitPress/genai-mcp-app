from faker import Faker
from db_conn import session
from db_conn import FinancialReport, IncomeStatement, BalanceSheet, CashFlowStatement, EquityStatement
from dtos.financial_report_dto import FinancialReportDTO, BalanceSheetDTO, IncomeStatementDTO, CashFlowStatementDTO, EquityStatementDTO
from repository import create_report, create_balance_sheet, create_income_statement, create_cashflow_statement, create_equity_statement

fake = Faker('en_US')


from faker import Faker

fake = Faker()

# Create 20 financial reports
for i in range(20):
    # Create income statement
    is_dto = IncomeStatementDTO(
        financial_report_id=i+1,
        revenue=fake.random_int(1000, 5000),
        cost_of_goods_sold=fake.random_int(1000, 5000),
        gross_profit=fake.random_int(1000, 5000),
        net_income=fake.random_int(1000, 5000)
    )
    is_obj = create_income_statement(is_dto)

    # Create balance sheet
    bs_dto = BalanceSheetDTO(
        financial_report_id=i+1,
        assets=fake.random_int(1000, 5000),
        liabilities=fake.random_int(2000, 5000),
        equity=fake.random_int(1000, 5000)
    )
    bs_obj = create_balance_sheet(bs_dto)

    # Create cash flow statement
    cs_dto = CashFlowStatementDTO(
        financial_report_id=i+1,
        operating_activities=fake.random_int(1000, 5000),
        investing_activities=fake.random_int(1000, 5000),
        financing_activities=fake.random_int(2000, 5000),
        net_cash_flow=fake.random_int(10000, 50000)
    )
    cs_obj = create_cashflow_statement(cs_dto)

    # Create equity statement
    es_dto = EquityStatementDTO(
        financial_report_id=i+1,
        beginning_equity=fake.random_int(1000, 5000),
        net_income=fake.random_int(1000, 5000),
        dividends=fake.random_int(1000, 5000),
        ending_equity=fake.random_int(1000, 5000)
    )
    es_obj = create_equity_statement(es_dto)

    # Create financial report
    fr_dto = FinancialReportDTO(
        company_name=fake.company(),
        year=fake.year(),
        period=fake.random_element(elements=("Annually", "Quarterly", "Monthly")),
        income_statement=is_obj,
        balance_sheet=bs_obj,
        cashflow_statement=cs_obj,
        equity_statement=es_obj
    )
    create_report(fr_dto)
