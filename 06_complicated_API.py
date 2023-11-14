from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

# バリデーション
# nameの文字数を規制する。
from pydantic import Field



class ShopInfo(BaseModel):
    name: str
    location: str 


# バリデーション
# = Field(min_length=4, max_length=12)
class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None
    
    
class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]
    
    
app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {"data": data}

