from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict, StringConstraints


QuestionText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=5, max_length=100)]
CategoryName = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=255)]


class CategoryBase(BaseModel):
    name: CategoryName


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: CategoryName | None = None


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class QuestionBase(BaseModel):
    text: QuestionText


class QuestionCreate(QuestionBase):
    category_id: Annotated[int, Field(gt=0)]


class QuestionUpdate(QuestionBase):
    text: QuestionText | None = None
    category_id: Annotated[int, Field(gt=0)] | None = None


class QuestionRead(QuestionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category: CategoryRead | None = None
