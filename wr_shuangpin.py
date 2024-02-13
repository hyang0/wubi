first_wr = {'ch': 'i',
            'sh': 'u',
            'zh': 'v'}

second_wr = {
    'ua': 'w',
    'ei': 'z',
    'e': 'e',
    'ou': 'b',
    'iu': 'q',
    've': 'v',
    'ue': 't',
    'u': 'u',
    'i': 'i',
    'o': 'o',
    'uo': 'o',
    'ie': 'x',
    'a': 'a',
    'ong': 's',
    'iong': 's',
    'ai': 'l',
    'ing': ';',
    'uai': 'y',
    'ang': 'h',
    'uan': 'r',
    'an': 'j',
    'en': 'f',
    'ia': 'w',
    'iang': 'd',
    'uang': 'd',
    'eng': 'g',
    'in': 'n',
    'ao': 'k',
    'v': 'v',
    'ui': 'v',
    'un': 'p',
    'iao': 'c',
    'ian': 'm'
}

# 特殊，只有䪨母，且总长不过 3
# 零声母，单双三䪨母
special_wr = {
    'a': 'oa',
    'ai': 'ol',
    'an': 'oj',
    'ang': 'oh',
    'ao': 'ok',
    'e': 'oe',
    'ei': 'oz',
    'en': 'of',
    'er': 'or',
    'o': 'oo',
    'ou': 'ob'
}


def to_double(s: str) -> str:
    """
    传入单汉字的全拼编码，返回其微软双拼编码

    :param s: 全拼编码
    :return: 双拼编码
    """
    new_s = ''
    # 特列情况: 无声母，a, an, ang
    if len(s) <= 3 and s[0] in ['a', 'e', 'o']:
        if s in special_wr.keys():
            return special_wr[s]
        else:
            return s

    # 一般: 声母 + 䪨母

    # 最长的情况：first_wr+second_wr，例如 chuang = ch + uang
    # 2 位声母 + 最多 4 位韵母
    if s[:2] in first_wr.keys():
        new_s += first_wr[s[:2]]
        # 最多 4 位䪨母
        if s[2:] in second_wr.keys():
            new_s += second_wr[s[2:]]
    # 较短的情况：second_wr+second_wr，例如 h uang, x iang
    # 1 位声母 + 最多 4 位䪨母
    else:
        new_s += s[0]  # 1 位声母
        # 最多 4 位䪨母
        if s[1:] in second_wr.keys():
            new_s += second_wr[s[1:]]
        else:
            new_s += s[1:]

    return new_s

"""  """
if __name__ == '__main__':
    """ 测试函数 """
    pinyin = '（'
    shuangpin = to_double(pinyin)
    print(f"The Shuangpin encoding for '{pinyin}' is '{shuangpin}'.")
