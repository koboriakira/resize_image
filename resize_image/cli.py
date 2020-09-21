import argparse
from resize_image.resize import resize


def execute():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'img',
        help='ファイルを指定',
        type=str,
        default='')
    args = parser.parse_args()
    resize(args.img)


execute()
