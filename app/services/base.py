from abc import abstractmethod

class Base:
    @abstractmethod
    async def get():
        pass
    @abstractmethod
    async def add():
        pass