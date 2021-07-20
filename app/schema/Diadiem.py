from pydantic import BaseModel


class Diadiem(BaseModel):
    id: str
    ten: str


class DiadiemDto(BaseModel):
    id: str
    ten: str

    class Config:
        orm_mode = True