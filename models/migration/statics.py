from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

# class MyDataModel(BaseModel):
    # id: Optional[str] = Field(None, alias='_id')
    # name: str
    # age: int
    # email: str

    # class Config:
    #     json_encoders = {
    #         ObjectId: str
    #     }

