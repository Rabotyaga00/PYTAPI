import requests
import json

def get_all_posts():
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x)

get_all_posts()
