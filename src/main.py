from fastapi import FastAPI
from router.mcpRouter import mcpRouter
app = FastAPI()
app.include_router(mcpRouter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app" , host="0.0.0.0" , port=8080 , reload=True)
    
