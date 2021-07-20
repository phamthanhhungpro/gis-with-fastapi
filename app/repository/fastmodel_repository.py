from typing import Optional, List

from sqlalchemy.orm import Session
from app.models.model import Diadiem, Fastmodel
from app.repository.base_repository import BaseRepository

class FastmodelRepository(BaseRepository[Fastmodel, Fastmodel, Fastmodel]):
    # Declare model specific CRUD operation methods.
    pass


fastmodelRepository = FastmodelRepository(Fastmodel)