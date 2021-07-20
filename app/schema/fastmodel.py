from pydantic import BaseModel


class Fastmodel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
