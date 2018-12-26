import requests

response = requests.get('https://api.myip.com').json()
print('Public IP address: {}\nCountry: {}\n'.format(response['ip'],response['country']))
