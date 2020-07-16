import argparse

import pngdata


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
    pngdata.encode(text, args.file)
    args.file.close()
    print('Success')
elif args.action == 'd':
    print(pngdata.decode(args.file))
else:
    parser.print_help()
