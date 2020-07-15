from abc import ABC, abstractstaticmethod
from typing import BinaryIO, Union


class PluginABC(ABC):

    @abstractstaticmethod
    def decode(fp: BinaryIO) -> Union[str, bytes]:
        pass

    @abstractstaticmethod
    def encode(data: Union[str, bytes]) -> BinaryIO:
        pass
