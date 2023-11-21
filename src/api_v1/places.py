from fastapi import APIRouter

router = APIRouter(prefix="/places", tags=['places'])


@router.post('/')
async def create_place():
    ...


@router.get('/{place_id}')
async def get_one_place(place_id):
    ...


@router.get('/')
async def get_all_places():
    ...


@router.delete('/{place_id}')
async def del_one_place(place_id):
    ...


@router.patch('/{place_id}')
async def update_one_place(place_id):
    ...
