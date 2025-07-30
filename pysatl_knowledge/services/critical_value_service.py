from typing import Optional

from fastapi import HTTPException

from pysatl_knowledge.models.critical_value_model import CriticalValueModel
from pysatl_knowledge.repositories import CriticalValueRepository
from pysatl_knowledge.schemas.critical_value_schema import (
    CriticalValueCreate,
    CriticalValueResponse,
)


class CriticalValuesService:
    def __init__(self):
        self.repository = CriticalValueRepository()

    async def get_cv_by_params(
        self,
        criterion_code: Optional[str] = None,
        sample_size: Optional[int] = None,
        iterations: Optional[int] = None,
        status: Optional[str] = None,
    ) -> list[CriticalValueResponse]:
        critical_values = await self.repository.find_by_params(
            criterion_code=criterion_code,
            sample_size=sample_size,
            iterations=iterations,
            status=status,
        )
        if not critical_values:
            raise HTTPException(status_code=404, detail="No critical values found")

        return list(
            map(
                lambda cv: CriticalValueResponse(
                    id=cv.id,
                    criterion_code=cv.criterion_code,
                    sample_size=cv.sample_size,
                    iterations=cv.iterations,
                    result=cv.result,
                    status=cv.status,
                ),
                critical_values,
            )
        )

    async def create_cv(self, data: CriticalValueCreate) -> CriticalValueResponse:
        exp = CriticalValueModel(
            criterion_code=data.criterion_code,
            sample_size=data.sample_size,
            iterations=data.iterations,
            result=data.result,
            status="created",
        )
        exp = await self.repository.create(exp)
        return CriticalValueResponse(
            id=exp.id,
            criterion_code=exp.criterion_code,
            sample_size=exp.sample_size,
            iterations=exp.iterations,
            result=exp.result,
            status=exp.status,
        )

    async def verify_cv(self, experiment_id: int, status: str) -> Optional[CriticalValueResponse]:
        exp = await self.repository.find_by_id(experiment_id)
        if not exp:
            return None

        exp = await self.repository.update_status(exp, status)
        return CriticalValueResponse(
            id=exp.id,
            criterion_code=exp.criterion_code,
            sample_size=exp.sample_size,
            iterations=exp.iterations,
            result=exp.result,
            status=exp.status,
        )
