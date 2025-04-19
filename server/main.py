from flask import request, jsonify, Flask
from repository import create_report, create_balance_sheet, create_income_statement, create_cashflow_statement, create_equity_statement, find_report
from dtos.financial_report_dto import FinancialReportDTO, BalanceSheetDTO, IncomeStatementDTO, CashFlowStatementDTO, EquityStatementDTO

app = Flask(__name__)



"""
End points to create reports
"""

@app.route('/reports', methods=['POST'])
def create_report_endpoint():
    data = request.get_json()
    fr_dto = FinancialReportDTO(**data)

    # Check if balance sheet and other parameters are null
    if not fr_dto.balance_sheet or not fr_dto.income_statement or not fr_dto.cashflow_statement or not fr_dto.equity_statement:
        return jsonify({'error': 'Balance sheet, income statement, cash flow statement, and equity statement must be created first'}), 400

    create_report(fr_dto)
    return jsonify({'message': 'Report created successfully'}), 201

@app.route('/balance-sheets', methods=['POST'])
def create_balance_sheet_endpoint():
    data = request.get_json()
    bs_dto = BalanceSheetDTO(**data)

    # Check if financial report id is null
    if bs_dto.financial_report_id is None:
        return jsonify({'error': 'Financial report id must be provided'}), 400

    create_balance_sheet(bs_dto)
    return jsonify({'message': 'Balance sheet created successfully'}), 201


@app.route('/income-statements', methods=['POST'])
def create_income_statement_endpoint():
    data = request.get_json()
    is_dto = IncomeStatementDTO(**data)

    # Check if financial report id is null
    if is_dto.financial_report_id is None:
        return jsonify({'error': 'Financial report id must be provided'}), 400

    create_income_statement(is_dto)
    return jsonify({'message': 'Income statement created successfully'}), 201


@app.route('/cash-flow-statements', methods=['POST'])
def create_cash_flow_statement_endpoint():
    data = request.get_json()
    cs_dto = CashFlowStatementDTO(**data)

    # Check if financial report id is null
    if cs_dto.financial_report_id is None:
        return jsonify({'error': 'Financial report id must be provided'}), 400

    create_cashflow_statement(cs_dto)
    return jsonify({'message': 'Cash flow statement created successfully'}), 201


@app.route('/equity-statements', methods=['POST'])
def create_equity_statement_endpoint():
    data = request.get_json()
    es_dto = EquityStatementDTO(**data)

    # Check if financial report id is null
    if es_dto.financial_report_id is None:
        return jsonify({'error': 'Financial report id must be provided'}), 400

    create_equity_statement(es_dto)
    return jsonify({'message': 'Equity statement created successfully'}), 201



"""
End points to get reports
"""

@app.route('/reports', methods=['GET'])
def get_reports():
    data = request.get_json()
    print(data)
    financial_report = find_report(data['company_name'], data['year'], data['period'])
    res = {
        "company_name": financial_report.company_name,
        "year": financial_report.year,
        "period": financial_report.period,
        "balance_sheet": {
            "assets": financial_report.balance_sheet.assets,
            "liabilities": financial_report.balance_sheet.liabilities,
            "equity": financial_report.balance_sheet.equity
        },
        "income_statement": {
            "revenue": financial_report.income_statement.revenue,
            "cost_of_goods_sold": financial_report.income_statement.cost_of_goods_sold,
            "gross_profit": financial_report.income_statement.gross_profit,
            "net_income": financial_report.income_statement.net_income
        },
        "cashflow_statement": {
            "operating_activities": financial_report.cashflow_statement.operating_activities,
            "investing_activities": financial_report.cashflow_statement.investing_activities,
            "financing_activities": financial_report.cashflow_statement.financing_activities,
            "net_cash_flow": financial_report.cashflow_statement.net_cash_flow
        },
        "equity_statement": {
            "equity": financial_report.equity_statement.beginning_equity,
            "net_income": financial_report.equity_statement.net_income,
            "dividends": financial_report.equity_statement.dividends,
            "ending_equity": financial_report.equity_statement.ending_equity
        }
    }
    return jsonify(res), 200



if __name__ == '__main__':
    app.run(debug=True)