from abc import ABC, abstractmethod


class BaseDBRepository(ABC):
    """Базовый абстрактный репозиторий для работы с отдельно взятой таблицей БД"""

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def get_many(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def update(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, *args, **kwargs):
        raise NotImplementedError()
