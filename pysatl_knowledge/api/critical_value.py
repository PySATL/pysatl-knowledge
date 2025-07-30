from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Path

from pysatl_knowledge.core.security.jwt_utils import get_current_admin, get_current_user
from pysatl_knowledge.schemas.critical_value_schema import (
    CriticalValueCreate,
    CriticalValueResponse,
    CriticalValueVerify,
)
from pysatl_knowledge.services.critical_value_service import CriticalValuesService
from pysatl_knowledge.services.dependencies import get_cv_service


router = APIRouter(prefix="/critical_values", tags=["Critical Values"])


@router.get("", response_model=CriticalValueResponse)
async def get_critical_values(
    criterion_code: str,
    size: int,
    iterations: int,
    service: CriticalValuesService = Depends(get_cv_service),
):
    return (
        await service.get_cv_by_params(
            criterion_code=criterion_code,
            sample_size=size,
            iterations=iterations,
            status="verified",
        )
    )[0]


@router.get("/all", response_model=list[CriticalValueResponse])
async def get_all_critical_values(
    criterion_code: Optional[str] = None,
    size: Optional[int] = None,
    iterations: Optional[int] = None,
    status: Optional[str] = None,
    current_user=Depends(get_current_user),
    service: CriticalValueCreate = Depends(get_cv_service),
):
    return await service.get_cv_by_params(
        criterion_code=criterion_code,
        sample_size=size,
        iterations=iterations,
        status=status,
    )


@router.post("", response_model=CriticalValueResponse)
async def create_critical_value(
    data: CriticalValueCreate, service: CriticalValuesService = Depends(get_cv_service)
):
    """
    Создать новое критическое значение.
    """
    try:
        return await service.create_cv(data)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.patch("/{critical_value_id}/verify", response_model=CriticalValueResponse)
async def verify_critical_value(
    data: CriticalValueVerify,
    critical_value_id: int = Path(..., ge=1),
    service: CriticalValuesService = Depends(get_cv_service),
    current_admin=Depends(get_current_admin),
):
    """
    Верифицировать или отклонить критическое значение (только для admin).
    """
    result = await service.verify_cv(critical_value_id, data.status)
    if not result:
        raise HTTPException(status_code=404, detail="Critical value not found")
    return result
