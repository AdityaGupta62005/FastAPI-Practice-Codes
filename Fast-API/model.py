from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    des: str
    price: float
    quantity: int 