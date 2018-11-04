import requests
import random

subscription_key = 'a6a9a80426344c689f6733b4772d1702'
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"

def search_image_get_url(search_term): 
	headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
	params  = {"q": search_term, "license": "public", "imageType": "photo"}
	response = requests.get(search_url, headers=headers, params=params)
	response.raise_for_status()
	search_results = response.json()

	thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]

	return (search_results['value'][random.randint(0, 34)]['contentUrl'])
	# 35 queries in total
	# returns the url

# print(search_image_get_url('cute animal'))
