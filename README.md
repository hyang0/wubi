# wubi

显示汉字的拼音和五笔编码

用法：

```bash
$ pip install -r requirement.txt

$ python wubi.py -h
usage: wubi.py [-h] [--wubi_file WUBI_FILE]
               FILE or character [FILE or character ...]

汉字拼音和五笔编码查询工具

positional arguments:
  FILE or character     文件路径或要转换的汉字

options:
  -h, --help            show this help message and exit
  --wubi_file WUBI_FILE
                        五笔编码文件路径，默认为 wubi86.dict

$ python wubi.py 百家姓.txt | head
汉字: 赵钱孙李
拼音: zhao qian sun li
双拼: vk qm sp li
五笔: fhqi qgt biy sbf

汉字: 周吴郑王
拼音: zhou wu zheng wang
双拼: vb wu vg wh
五笔: mfkd kgdu udbh gggg

$ python wubi.py 鸟 曹操 龟鬼雨鱼羽
汉字: 鸟
拼音: niao
双拼: nc
五笔: qyng

汉字: 曹操
拼音: cao cao
双拼: ck ck
五笔: gmaj rkks

汉字: 龟鬼雨鱼羽
拼音: gui gui yu yu yu
双拼: gv gv yu yu yu
五笔: qjnb rqci fghy qgf nnyg

$ python wubi.py 微软 双拼
汉字: 微软
拼音: wei ruan
双拼: wz rr
五笔: tmgt lqwy

汉字: 双拼
拼音: shuang pin
双拼: ud pn
五笔: ccy ruah


```

此处的双拼方案是微软双拼

## 参考

- https://github.com/bcaso/pinyin_to_double_pinyin
- https://github.com/Yidadaa/shuangpin
- https://github.com/rime/rime-wubi