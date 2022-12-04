from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def canBeUpgraded(self):
        pass