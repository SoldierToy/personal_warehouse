from src.repositories.base_repository import SQLAlchemyRepository
from src.models.places import PlacesORM


class PlacesRepository(SQLAlchemyRepository):
    model = PlacesORM
