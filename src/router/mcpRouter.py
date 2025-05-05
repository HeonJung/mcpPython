from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from .model.mcpBaseModels import mcpServer
from .services.mcpServices import mcpJson

mcpRouter = APIRouter()

@mcpRouter.post('/addmcp')
async def addMcpItem(mcpItem : mcpServer):
    print("data : " , mcpItem)
    jsonStatus = mcpJson(jsonable_encoder(mcpItem))
    # print(jsonStatus)
    return jsonStatus

