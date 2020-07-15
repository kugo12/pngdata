from abc import ABC, abstractmethod
from typing import BinaryIO, Tuple


class PluginABC(ABC):

    @staticmethod
    @abstractmethod
    def decode(fp: BinaryIO) -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def encode(data: str) -> Tuple[BinaryIO, str]:
        raise NotImplementedError
