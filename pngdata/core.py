from PIL import Image
from io import BytesIO
from math import sqrt, ceil
from typing import BinaryIO, Union, Optional


def decode(fp: Union[BinaryIO, str], string: bool = True) -> Union[str, bytes]:
    """Decodes png file to bytes or string

    Args:
        fp: file like object or path.
        string: whether return UTF-8 string or raw bytes.

    Returns:
        UTF-8 string or bytes object.

    """
    img = Image.open(fp)
    data = img.tobytes()

    if string:
        data = data.decode('utf-8')
    return data


def encode(data: Union[str, bytes],
           fp: Optional[Union[BinaryIO, str]] = None
           ) -> Union[BinaryIO, str]:
    """Encode data to fp

    Args:
        data: utf-8 string or raw bytes.
        fp: optional file like object or path.

    Returns:
        fp if supplied, else BytesIO with png image.

    """
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
    img.save(fp, 'png', quality=100)

    return fp
