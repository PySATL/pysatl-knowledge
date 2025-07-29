from sqlalchemy.future import select

from pysatl_knowledge.core.database import async_session
from pysatl_knowledge.models import User


class UserRepository:
    async def find_by_username(self, username: str) -> User | None:
        """
        Find a user by their username.
        :param username: The username of the user to find.
        :return: A User object if found, otherwise None.
        """
        async with async_session() as session:
            result = await session.execute(select(User).where(User.username == username))
            return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        """
        Create a new user in the database.
        :param user: The User object to create.
        :return: The created User object with its ID populated.
        """
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, user: User) -> User:
        """
        Update an existing user in the database.
        :param user: The User object to update.
        :return: The updated User object.
        """
        async with async_session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def delete_by_id(self, user_id: int) -> bool:
        """
        Delete a user by their ID.
        :param user_id: The ID of the user to delete.
        :return: True if the user was deleted, otherwise False.
        """
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()
            if user is None:
                return False
            await session.delete(user)
            await session.commit()
            return True
