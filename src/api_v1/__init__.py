from fastapi import APIRouter

from .places import router as places_router
from .products import router as products_router
from .products_types import router as products_types_router
from .products_locations import router as products_locations_router
from .statuses import router as statuses_router
from .users import router as users_router


router = APIRouter()
router.include_router(router=places_router)
router.include_router(router=products_router)
router.include_router(router=products_types_router)
router.include_router(router=products_locations_router)
router.include_router(router=statuses_router)
router.include_router(router=users_router)