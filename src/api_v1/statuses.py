from fastapi import APIRouter

router = APIRouter(prefix="/statuses", tags=['statuses'])


@router.post('/')
async def create_status():
    ...


@router.get('/{status_id}')
async def get_one_status(status_id):
    ...


@router.get('/')
async def get_all_statuses():
    ...


@router.delete('/{status_id}')
async def del_one_status(status_id):
    ...


@router.patch('/{status_id}')
async def update_one_status(status_id):
    ...
