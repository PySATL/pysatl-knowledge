from typing import Optional

from pydantic import BaseModel, confloat, conint, constr


class CriticalValueBase(BaseModel):
    code: type[str] = constr(min_length=1)
    size: type[int] = conint(gt=0)
    sl: type[float] = confloat(ge=0.0, le=1.0)
    lower_value: float
    upper_value: Optional[float] = None


class CriticalValueCreate(CriticalValueBase):
    pass


class CriticalValueResponse(CriticalValueBase):
    id: int
    status: str
    created_by: Optional[int] = None

    class Config:
        from_attributes = True


class CriticalValueVerify(BaseModel):
    status: str
