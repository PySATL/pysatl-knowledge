from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query

from pysatl_knowledge.core.security import get_current_admin, get_current_user
from pysatl_knowledge.schemas.critical_value import (
    CriticalValueCreate,
    CriticalValueResponse,
    CriticalValueVerify,
)
from pysatl_knowledge.services.dependencies import get_cv_service


router = APIRouter(prefix="/critical_values", tags=["Critical Values"])


@router.get("", response_model=CriticalValueResponse)
async def get_critical_values(
    code: Optional[str] = Query(None),
    size: Optional[int] = Query(None),
    sl: Optional[float] = Query(None),
    service: CriticalValueCreate = Depends(get_cv_service),
):
    """
    Получить список критических значений с фильтрацией по code/size/sl.
    """
    return await service.get_cv_by_params(code=code, size=size, sl=sl)


@router.post("", response_model=CriticalValueResponse)
async def create_critical_value(
    data: CriticalValueCreate,
    service: CriticalValueCreate = Depends(get_cv_service),
    current_user=Depends(get_current_user),
):
    """
    Создать новое критическое значение.
    """
    try:
        return await service.create_cv(data, created_by=current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.patch("/{critical_value_id}/verify", response_model=CriticalValueResponse)
async def verify_critical_value(
    data: CriticalValueVerify,
    critical_value_id: int = Path(..., ge=1),
    service: CriticalValueCreate = Depends(get_cv_service),
    current_admin=Depends(get_current_admin),
):
    """
    Верифицировать или отклонить критическое значение (только для admin).
    """
    result = await service.verify_cv(critical_value_id, data.status)
    if not result:
        raise HTTPException(status_code=404, detail="Critical value not found")
    return result
