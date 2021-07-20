from typing import Any, List

from starlette.responses import JSONResponse
from app.schema.Diadiem import Diadiem, DiadiemDto
from app.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.repository.diadiem_repository import diadiemRepository
router = APIRouter()


@router.get("", response_model=List[DiadiemDto])
async def getDiadiem(db: Session = Depends(get_db)):
    item = diadiemRepository.get_table(db).limit(10)
    listItem = list(item)
    return listItem

@router.get("/rawsql", response_model=List[DiadiemDto])
async def get_raw(db: Session = Depends(get_db)):
    response_model=list[DiadiemDto]()
    item = db.execute("select * from diadiem")
    for row in item:
        temp = DiadiemDto
        temp.id = str(row["id"])
        temp.ten = row["ten"]

        response_model.append(temp)
    return response_model

@router.get("/id", response_model=DiadiemDto)
async def get_diadiem_by_id(*, db: Session = Depends(get_db), id: str):
    item = diadiemRepository.get(db, id)
    return item

@router.post("")
def create_diadiem(*, db: Session = Depends(get_db), inputModel: Diadiem) -> Any:
    diadiemRepository.create(db, obj_in=inputModel)
    return JSONResponse(status_code=status.HTTP_201_CREATED)

@router.put("")
def update_diadiem(*, db: Session = Depends(get_db), updateModel: Diadiem) -> Any:
    model = diadiemRepository.get(db, model_id=updateModel.id)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tồn tại dữ liệu !!!",
        )
    diadiemRepository.update(db, db_obj=model, obj_in=updateModel)
    return JSONResponse(status_code=status.HTTP_200_OK)

@router.delete("")
def delete_diadiem(*, db: Session = Depends(get_db), id: str):
    model = diadiemRepository.get(db, model_id=id)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    diadiemRepository.remove(db, model_id=model.id)
    return {"message": f"Product with ID = {id} deleted."}


