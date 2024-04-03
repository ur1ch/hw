from fastapi import APIRouter
from typing import Annotated
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("")
def get_items_list():
    return {
        "data": [
            {"id": 1, "name": "item 1"},
            {"id": 2, "name": "item 2"},
        ]

    }

@router.get("/{item_id}")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"item {item_id}",
        }
    }


class ItemCreate(BaseModel):
    name: str
    description: str

@router.post("")
def create_item(
        item: ItemCreate,
):
    return {
        "data": {
            "id": 0,
            "name": item.name,
            "description": item.description,
        },
    }
