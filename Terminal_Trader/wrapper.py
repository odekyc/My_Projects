import requests

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def company_search(self,companyname):
		mydic=dict(input=companyname)
		r=requests.get(url=self.lookup_url, params=mydic)
		result=r.json()
		if (len(result)==0 or len(result)>6):
			return False
		else:
			return result

	def get_quote(self,symbol):
		r=requests.get(url=self.quote_url+symbol)
		result=r.json()
		
		if(len(result)<3):
			return False
		else:
			return result

'''markit=Markit()
googleresult=markit.company_search('Google')
print (googleresult)

print (markit.get_quote('GOOG'))'''