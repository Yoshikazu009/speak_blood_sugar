#Nightscout API Class
import requests
class Nightscout_API:
	url = None	#Nightscout User URL格納変数
	#最新の血糖値を取得
	def get_sgv(self):
		base_url = self.url + "/api/v1/entries.json?count=100" #過去100件の血糖値
		r = requests.get(base_url)
		j = r.json()
		sgv = j[0]['sgv'] #最新の血糖値
		return sgv
	
