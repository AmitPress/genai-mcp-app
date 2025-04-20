""" This MCP server will talk to the database via the REST API provided by the flask server running at port 5000. """

from mcp.server.fastmcp import FastMCP
import requests
app = FastMCP("Company Details")

@app.tool()
def company_details(company_name, year):
    res = requests.get("http://localhost:5000/reports", json={"company_name": company_name, "year": year, "period": "Yearly"})
    data = res.json()
    return str(data)

if __name__ == "__main__":
    app.run(transport="stdio")
