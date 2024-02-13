import argparse
from pypinyin import pinyin, Style
import platform
import os
import sys


def change_default_encoding():
    '''判断是否在 windows git-bash 下运行，是则使用 utf-8 编码'''
    if platform.system() == 'Windows':
        terminal = os.environ.get('TERM')
        if terminal and 'xterm' in terminal:
            sys.stdout.reconfigure(encoding='utf-8')


def is_empty_line(line):
    return line.isspace()


def load_wubi_dict(file_path):
    wubi_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            char, wubi_code = line.strip().split(' ')
            wubi_dict[char] = wubi_code
    return wubi_dict


def get_pinyin(character):
    pinyin_result = pinyin(character, style=Style.NORMAL)
    pinyin_str = ''.join([item[0] for item in pinyin_result])
    return pinyin_str


def get_wubi(character, wubi_dict):
    wubi_str = wubi_dict.get(character)
    if not wubi_str:
        return character
    return wubi_str


def cout(characters):
    """ 输出 """
    py_list = []
    wb_list = []

    for char in characters:
        pinyin_result = get_pinyin(char)
        wubi_result = get_wubi(char, wubi_dict)

        py_list.append(pinyin_result)
        wb_list.append(wubi_result)

    print("汉字:", characters)
    print("拼音:", ' '.join(py_list))
    print("五笔:", ' '.join(wb_list))
    print()


def process_file(file_path):
    """ 处理文件 """
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            characters = line.strip()
            if is_empty_line(line):
                continue
            cout(characters)


def process_character(line):
    """ 处理汉字 """
    characters = line.strip()
    cout(characters)


def file_exists(file_path):
    return os.path.exists(file_path)


if __name__ == "__main__":
    change_default_encoding()
    parser = argparse.ArgumentParser(description="汉字拼音和五笔编码查询工具")
    parser.add_argument("file_path", metavar='FILE or character',
                        nargs='+', help="文件路径或要转换的汉字")
    parser.add_argument("--wubi_file", default=r"wubi86.dict",
                        help="五笔编码文件路径，默认为 wubi86.dict")
    args = parser.parse_args()

    wubi_dict = load_wubi_dict(args.wubi_file)

    for line in args.file_path:
        if file_exists(line):
            process_file(line)
        else:
            process_character(line)
