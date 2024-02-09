# wubi

显示汉字的拼音和五笔编码

用法：

```bash
bash$ python wubi.py -h
usage: wubi.py [-h] [--wubi_file WUBI_FILE] file_path

汉字拼音和五笔编码查询工具

positional arguments:
  file_path             包含汉字的文件路径

options:
  -h, --help            show this help message and exit
  --wubi_file WUBI_FILE
                        五笔编码文件路径，默认为 wubi86.dict

bash$ python wubi.py 百家姓.txt | head
汉字: 赵钱孙李
拼音: zhao qian sun li
五笔: fhqi qgt biy sbf

汉字: 周吴郑王
拼音: zhou wu zheng wang
五笔: mfkd kgdu udbh gggg

```
