## speak_blood_sugar
現在の血糖値を音声で応えるスクリプト
「Hey Siri 血糖値を教えて」と聞くと、nightscoutから最新の血糖値を取得して「血糖は○○○です。」「血糖は低血糖です。」と音声で応える。

[speak_blood_sugar デモ画面](https://twitter.com/takobouzu00/status/1549169086948872192?s=21&t=t9s2WZuuHtxIFTRZDKIujA)

## 動作環境
- iOS 15.6
- pythonista3 3.3
## インストール
### ファイル配置
pythonista3で下記のファイルを「iCloud/speak_blood_sugar」にインポートする。
- speak_blood_sugar.py
- nightscout_api.py
- 
### ショートカット作成

iOSのショートカットを作成することで、Siriが音声認識で「血糖値を教えて」を認識して、対応するpythonista3スクリプトを実行することができる。
pythonista3u

#### pythonisata3でスクリプトの実行URLを取得する。

![ショートカットからURLを取得](https://user-images.githubusercontent.com/108761384/179634718-3373481f-3b86-4ee1-9f2e-d3d761c42bb8.png)

![ショートカットからURLを取得2](https://user-images.githubusercontent.com/108761384/179635675-fb391f3d-fd47-45ac-97d7-b361c3e9165f.png)

#### iOSでショートカット「血糖値を教えて」を作成する。

![血糖値を教えて](https://user-images.githubusercontent.com/108761384/179632536-b2fb3575-733a-4ffc-b9a7-63e0f1acc33a.png)

- タイトルを「血糖値を教えて」と定義する。Siriがタイトルを音声認識してスクリプトを実行する。
- WEBを選択して「pythonista3://iCloud/speak_blood_sugar/speak_blood_sugar.py?action=run」を開くを定義する。



## 開発来歴
- 2022.07.18 新規開発　たかしま・よしかず
## ライセンス
MIT License
Copyright (c) 2022 たかしま・よしかず
