#speak_blood_sugar.py
#Nightscoutから最新の血糖値を取得して音声出力するスクリプト 
#pythonisat3 3.3
import speech #Speech Class
import nightscout_api #Nightscout API Class
api = nightscout_api.Nightscout_API() #Nightscout APIインスタンス
api.url = 'https://xxxxxxxx.herokuapp.com' #Nightscout url設定
sgv = api.get_sgv() #最新の血糖値を取得
speak_msg = '現在の血糖は' + sgv + 'です。'
speech.say(speak_msg) #最新の血糖値を喋る
speak_msg = '血糖は正常です。'
if int(sgv) > 199:
	speak_msg = '血糖は高血糖です。'
if int(sgv) < 80:
	speak_msg = '血糖は低血糖です。'
speech.say(speak_msg) #血糖値の判定結果を喋る
#
