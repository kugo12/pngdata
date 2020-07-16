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
        img.save(fp, 'png', quality=100)

        return fp


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='actions', dest='action')

    parser_encode = subparsers.add_parser('e', help='encode')
    parser_encode.add_argument('file', help='path to file', type=argparse.FileType('wb'))
    parser_encode.add_argument('text', help='text to encode', nargs='+')

    parser_decode = subparsers.add_parser('d', help='decode')
    parser_decode.add_argument('file', help='path to file', type=argparse.FileType('rb'))

    args = parser.parse_args()

    if args.action == 'e':
        text = ' '.join(args.text)
        PNGData.encode(text, args.file)
        args.file.close()
        print('Success')
    elif args.action == 'd':
        print(PNGData.decode(args.file))
    else:
        parser.print_help()
