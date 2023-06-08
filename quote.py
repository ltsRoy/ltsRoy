import os
import requests

category = 'computers'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
api_key = os.environ.get('API_KEY')
headers = {'X-Api-Key': api_key}

response = requests.get(api_url, headers=headers)
if response.status_code == requests.codes.ok:
    json_data = response.json()
    if json_data:
        data = json_data[0]
        quote = data.get('quote')
        author = data.get('author')

        formatted_output = f"{quote} - {author}"
        print(formatted_output)
    else:
        print("No quotes found.")
else:
    print("Error:", response.status_code, response.text)
