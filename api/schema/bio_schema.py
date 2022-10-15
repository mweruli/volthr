
from typing import Optional
from pydantic import BaseModel,Field

class AddDetails(BaseModel):
    sn: str = Field(
        default=None, title="sn"
    )
    alias: str = Field(
        default=None, title="alias"
    )
    ip_address: str = Field(
        default=None, title="ip_address"
    )
    terminal_tz: int = Field(
        default=None, title="terminal_tz"
    )
    heartbeat: int = Field(
        default=None, title="sn"
    )
    area: int = Field(
        default=None, title="alias"
    )
    
class AddArea(BaseModel):
    area_code: str
    area_name: str
    parent_area: int
    class Config:
        orm_mode = True
        
class UpdateArea(BaseModel):
    area_code: Optional[str]
    area_name: Optional[str]
    parent_area: Optional[str]