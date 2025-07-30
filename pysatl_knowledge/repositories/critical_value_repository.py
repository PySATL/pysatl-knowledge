from typing import Optional

from sqlalchemy.future import select

from pysatl_knowledge.core.database import async_session
from pysatl_knowledge.models import CriticalValueModel


class CriticalValueRepository:
    async def find_by_params(
        self,
        criterion_code: Optional[str] = None,
        sample_size: Optional[int] = None,
        iterations: Optional[int] = None,
        status: Optional[str] = None,
    ) -> list[CriticalValueModel]:
        """
        Find experiments by criterion code, sample size, and iterations.
        :param criterion_code: The code of the criterion to filter experiments.
        :param sample_size: The sample size of the experiments to filter.
        :param iterations: The number of iterations of the experiments to filter.
        :param status: The status of the experiments to filter.
        :return: A list of Experiment objects that match the given parameters.
        """
        async with async_session() as session:
            query = select(CriticalValueModel)
            if criterion_code is not None:
                query = query.where(CriticalValueModel.criterion_code == criterion_code)
            if sample_size is not None:
                query = query.where(CriticalValueModel.sample_size == sample_size)
            if iterations is not None:
                query = query.where(CriticalValueModel.iterations == iterations)
            if status is not None:
                query = query.where(CriticalValueModel.status == status)

            result = await session.execute(query)
            return result.scalars().all()

    async def find_by_id(self, cv_id: int) -> CriticalValueModel | None:
        """
        Find an experiment by its ID.
        :param id: The ID of the experiment to find.
        :return: An Experiment object if found, otherwise None.
        """
        async with async_session() as session:
            result = await session.execute(
                select(CriticalValueModel).where(CriticalValueModel.id == cv_id)
            )
            return result.scalar_one_or_none()

    async def get_status(
        self, criterion_code: str, sample_size: int, iterations: int
    ) -> str | None:
        """
        Get the status of an experiment based on its criterion code, sample size, and iterations.
        :param criterion_code: The code of the criterion to filter experiments.
        :param sample_size: The sample size of the experiments to filter.
        :param iterations: The number of iterations of the experiments to filter.
        :return: The status of the experiment if found, otherwise None.
        """
        async with async_session() as session:
            result = await session.execute(
                select(CriticalValueModel.status).where(
                    CriticalValueModel.criterion_code == criterion_code,
                    CriticalValueModel.sample_size == sample_size,
                    CriticalValueModel.iterations == iterations,
                )
            )
            return result.scalar_one_or_none()

    async def create(self, experiment: CriticalValueModel) -> CriticalValueModel:
        """
        Create a new experiment in the database.
        :param experiment: The Experiment object to create.
        :return: The created Experiment object with its ID populated.
        """
        async with async_session() as session:
            session.add(experiment)
            await session.commit()
            await session.refresh(experiment)
            return experiment

    async def update(self, experiment: CriticalValueModel) -> CriticalValueModel:
        """
        Update an existing experiment in the database.
        :param experiment: The Experiment object to update.
        :return: The updated Experiment object.
        """
        async with async_session() as session:
            session.add(experiment)
            await session.commit()
            await session.refresh(experiment)
            return experiment

    async def update_status(
        self, experiment: CriticalValueModel, new_status: str
    ) -> CriticalValueModel:
        """
        Update the status of an existing experiment.
        :param experiment: The Experiment object to update.
        :param new_status: The new status to set for the experiment.
        :return: The updated Experiment object with the new status.
        """
        experiment.status = new_status
        return await self.update(experiment)

    async def delete(self, experiment: CriticalValueModel) -> None:
        """
        Delete an experiment from the database.
        :param experiment: The Experiment object to delete.
        :return: None
        """
        async with async_session() as session:
            await session.delete(experiment)
            await session.commit()
