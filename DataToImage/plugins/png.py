from PIL import Image
from io import BytesIO
from math import sqrt, ceil
from typing import Tuple, BinaryIO

from ..abc import PluginABC
from ..data_to_image import DataToImage


@DataToImage.register_plugin()
class png(PluginABC):

    @staticmethod
    def decode(fp: BinaryIO) -> str:
        img = Image.open(fp)
        data = img.tobytes()
        return data.decode('utf-8')

    @staticmethod
    def encode(data: str) -> Tuple[BinaryIO, str]:
        data = data.encode('utf-8')
        size = ceil(sqrt(len(data)/4))
        missing_bytes = (size**2) * 4 - len(data)
        size = (size, size)

        data += b'\x00' * missing_bytes

        img = Image.frombytes('RGBA', size, data)
        f = BytesIO()
        img.save(f, 'png', quality=100)
        f.seek(0)

        return (f, '.png')
