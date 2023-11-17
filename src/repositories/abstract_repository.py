from abc import ABC, abstractmethod, abstractstaticmethod


class AbstractRepository(ABC):

    @abstractmethod
    @abstractstaticmethod
    async def add_one(self, data):
        raise NotImplementedError

    @abstractmethod
    @abstractstaticmethod
    async def find_all():
        raise NotImplementedError
