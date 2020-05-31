#print('Hello world')
#print(1*24)

from pathlib import Path

# ¥¥serverAはWindowsネットワークに対応したパス
# ログインが必要の場合ログインしたあと下記プログラム実行推奨
# print(list(Path(r'\\192.168.11.3\home\AtcoderLib').glob("*")))

import glob
import os

files = glob.glob("/home/ibtosm/work/zgit/atcoder_lib_py/Lib*")
for file in files:
    fnm = os.path.basename(file)
    print(f"1. [{fnm}](file:{file})")