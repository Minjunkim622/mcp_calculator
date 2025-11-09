from fastmcp import FastMCP

mcp = FastMCP("sum-mcp")

@mcp.tool
def add(a: int, b: int) -> int:
    "Add two numbers and return the sum."
    return a + b

if __name__ == "__main__":
    # Streamable HTTP로 노출
    mcp.run(transport="http", host="0.0.0.0", port=8000)
