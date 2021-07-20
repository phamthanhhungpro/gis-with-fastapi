from typing import Optional, List

from sqlalchemy.orm import Session
from app.models.model import Diadiem
from app.repository.base_repository import BaseRepository

class DiadiemRepository(BaseRepository[Diadiem, Diadiem, Diadiem]):
    # Declare model specific CRUD operation methods.
    pass


diadiemRepository = DiadiemRepository(Diadiem)
