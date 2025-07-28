from typing import Optional

from pysatl_knowledge.schemas.critical_value import CriticalValueCreate, CriticalValueResponse


class CriticalValuesService:
    def __init__(self):
        # В будущем: сюда можно передать session или репозиторий
        pass

    async def get_cv_by_params(
        self,
        code: str,
        size: int,
        sl: float,
    ) -> CriticalValueResponse:
        # TODO

        return CriticalValueResponse(
            id=1,
            code=code,
            size=size,
            sl=sl,
            lower_value=-1.96,
            upper_value=1.96,
            status="created",
            created_by=1,
        )

    async def create_cv(self, data: CriticalValueCreate, created_by: int) -> CriticalValueResponse:
        """
        Создает новый эксперимент (заглушка)
        """

        # TODO
        return CriticalValueResponse(
            id=1,
            code=data.code,
            size=data.size,
            sl=data.sl,
            lower_value=data.lower_value,
            upper_value=data.upper_value,
            status="created",
            created_by=created_by,
        )

    async def verify_cv(self, experiment_id: int, status: str) -> Optional[CriticalValueResponse]:
        """
        Верифицирует или отклоняет эксперимент (заглушка)
        """

        # TODO
        if experiment_id != 42:
            return None
        return CriticalValueResponse(
            id=1,
            code="code",
            size=42,
            sl=0.1,
            lower_value=-1.96,
            upper_value=1.96,
            status=status,
            created_by=1,
        )
