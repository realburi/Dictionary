import requests
import json
 
app_id = 'c48794c7'

app_key = 'c923db0e6560e737513fdec7e8de09c6'

language = 'en'

word_id = input("word: ")

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()

urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

#data = r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["notes"][0]["text"]



#print("code {}\n".format(r.status_code))
print(r.text)
#print(requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}))
#print(data)
