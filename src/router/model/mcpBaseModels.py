from pydantic import BaseModel

# {
#   "mcpServers": {
#     "playwright": {
#       "command": "npx",
#       "args": [
#         "@playwright/mcp@latest"
#       ]
#     }
#   }
# }


class McpConfig(BaseModel):
    command : str
    args : list[str]
    

class mcpPlaywright(BaseModel):
    playwright : McpConfig
    
class mcpServer(BaseModel):
    mcpServers : mcpPlaywright

    