from fastapi import APIRouter, status

router: APIRouter = APIRouter(prefix='/v1/products', tags=['Products'])


@router.get("", status_code=status.HTTP_200_OK)
async def get_products_list() -> None:
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_product() -> None:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product() -> None:
    pass
