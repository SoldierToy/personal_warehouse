from fastapi import APIRouter

router = APIRouter(prefix="/statuses", tags=['statuses'])


@router.get('/')
async def get_statuses():
    print("get_statuses")
