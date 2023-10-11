from fastapi import APIRouter, status

router: APIRouter = APIRouter(prefix='/users', tags=['Users'])


@router.get("", status_code=status.HTTP_200_OK)
async def get_users_list() -> None:
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_user() -> None:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user() -> None:
    pass
