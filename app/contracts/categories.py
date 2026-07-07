from pydantic import BaseModel
from app.schemas import *


class CategoryCreateRequest(CategoryCreate):
    pass


class CategoryUpdateRequest(CategoryUpdate):
    pass


class CategoryResponse(CategoryRead):
    pass


class CategoryListResponse(BaseModel):
    items: list[CategoryResponse]
    count: int
