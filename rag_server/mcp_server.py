""" This MCP server will talk to the database via the REST API provided by the flask server running at port 5000. """

from mcp.server.fastmcp import FastMCP
import requests
app = FastMCP("Time Teller")

@app.tool()
def company_details(company_name, year, period):
    print(f"Financial report for {company_name} in {year} {period}")
    res = requests.get("http://localhost:5000/reports", json={"company_name": company_name, "year": year, "period": period})
    data = res.json()
    print(data)
    return str(data)

if __name__ == "__main__":
    app.run(transport="stdio")
