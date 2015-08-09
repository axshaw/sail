import json, requests

# Get a webpage, this creates a Response object called "r"

url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310120?res=3hourly&key=cee0b1ec-a751-458a-894e-6aec68a91beb'


resp = requests.get(url=url)
data = json.loads(resp.text)

if('SiteRep' in data):
    print(data)
