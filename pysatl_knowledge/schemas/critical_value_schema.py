from pydantic import BaseModel


class CriticalValueBase(BaseModel):
    criterion_code: str
    sample_size: int
    iterations: int
    result: float


class CriticalValueCreate(CriticalValueBase):
    pass


class CriticalValueResponse(CriticalValueBase):
    id: int
    status: str

    class Config:
        from_attributes = True


class CriticalValueVerify(BaseModel):
    status: str
