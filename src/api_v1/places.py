from fastapi import APIRouter

router = APIRouter(prefix="/places", tags=['places'])


@router.get('/')
async def get_places():
    print("get_places")
