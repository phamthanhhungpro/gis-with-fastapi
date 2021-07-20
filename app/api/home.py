from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def getHome():
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/ping")
async def helloWorld():
    return {"message": "Hello World"}