from PIL import Image
from io import BytesIO
from math import sqrt, ceil
from typing import BinaryIO, Union, Optional


class PNGData():

    @staticmethod
    def decode(fp: BinaryIO, string=True) -> Union[str, bytes]:
        img = Image.open(fp)
        data = img.tobytes()

        if string:
            data = data.decode('utf-8')
        return data

    @staticmethod
    def encode(data: Union[str, bytes],
               fp: Optional[BinaryIO] = None
               ) -> BinaryIO:
        if isinstance(data, str):
            data = data.encode('utf-8')

        # always square image
        size = ceil(sqrt(len(data)/4))
        missing_bytes = (size**2) * 4 - len(data)
        size = (size, size)

        data += b'\x00' * missing_bytes

        img = Image.frombytes('RGBA', size, data)
        if fp is None:
            fp = BytesIO()
        fp.seek(0)
        img.save(fp, 'png', quality=100)
        fp.seek(0)

        return fp
