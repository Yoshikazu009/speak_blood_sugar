## speak_blood_sugar
現在の血糖値を音声で応えるスクリプト
「Hey Siri 血糖値を教えて」と聞くと、nightscoutから最新の血糖値を取得して「血糖は○○○です。」「血糖は低血糖です。」と音声で応える。

[speak_blood_sugar デモ画面](https://twitter.com/takobouzu00/status/1549169086948872192?s=21&t=t9s2WZuuHtxIFTRZDKIujA)

## 動作環境
- iOS 15.6
- pythonisata3 3.3
## インストール
### ファイル配置
pythonisata3で下記のファイルを「iCloud/speak_blood_sugar」にインポートする。
- speak_blood_sugar.py
- nightscout_api.py
### ショートカット作成
pythonisata3でスクリプトの実行URLを取得する。



iOSでショートカット「血糖値を教えて」を作成する。

![血糖値を教えて](https://user-images.githubusercontent.com/108761384/179632536-b2fb3575-733a-4ffc-b9a7-63e0f1acc33a.png)

- タイトルを「血糖値を教えて」と定義する。Siriがタイトルを音声認識してスクリプトを実行する。
- WEBを選択して「pythonista3://iCloud/speak_blood_sugar/speak_blood_sugar.py?action=run」を開くを定義する。



## 開発来歴
- 2022.07.18 新規開発　たかしま・よしかず
## ライセンス
MIT License
Copyright (c) 2022 たかしま・よしかず
