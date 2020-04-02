#print('Hello world')
#print(1*24)

from pathlib import Path

# ¥¥serverAはWindowsネットワークに対応したパス
# ログインが必要の場合ログインしたあと下記プログラム実行推奨
print(list(Path(r'\\192.168.11.3\home\AtcoderLib').glob("*")))
