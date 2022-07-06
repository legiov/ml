import requests
from pprint import pprint
from bs4 import BeautifulSoup
import time

from requests.sessions import should_bypass_proxies
import schedule

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

#response = requests.get(url)

#print(response.text)

#currencies = response.json()

#pprint(currencies)
#print(currencies['Valute']['CZK']['Name'])

#url = 'https://nplus1.ru/news/2021/10/11/econobel2021' 
#response = requests.get(url=url)

#print(response.text)
#page = BeautifulSoup(response.text, 'html.parser')
#print(page.title)
#print(page.title.text)
#print(page.find('h1').text)
#print(page.find('time').text)
#print(page.find('div', class_='body').text)

# def wiki_header(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     return soup.find('h1').text

# print(wiki_header('https://en.wikipedia.org/wiki/Operating_system'))


# url = 'https://en.wikipedia.org/wiki/List_of_programming_languages' 
# response = requests.get(url)
# page = BeautifulSoup(response.text, 'html.parser')
# links = page.find_all('a')

# print([link.text for link in links[500:510]])

# token = '88ee22d188ee22d188ee22d11b889409c3888ee88ee22d1e9740b58eed7b187946a256b'
# url = 'https://api.vk.com/method/users.get'
# params = {
#     'user_id':1,
#     'v': 5.95,
#     'fields': 'sex,bdate',
#     'access_token': token,
#     'lang': 'ru'
# }
# ids = ','.join(map(str, range(1, 500)))
# params = {
#     'user_ids':ids,
#     'v': 5.95,
#     'fields': 'sex,bdate',
#     'access_token': token,
#     'lang': 'ru'
# }

# response = requests.get(url, params=params)
# result = response.json()
# all = 0
# women = 0
# for row in result['response']:
#     if row['sex'] != 0:
#         all = all + 1
#         if row['sex'] == 1:
#             women = women + 1

# print(round(women/all, 2))

# token = '88ee22d188ee22d188ee22d11b889409c3888ee88ee22d1e9740b58eed7b187946a256b'
# url = 'https://api.vk.com/method/groups.getMembers'
# params = {'group_id': 'vk', 'v': 5.95, 'access_token': token} 

# response = requests.get(url, params=params)
# data = response.json()
# users_for_checking = data['response']['items'][0:20]
# print(users_for_checking)
# count = 5
# offset = 0
# user_ids = []
# max_count = 20
# while offset < max_count:
#     print(f"Выгружаю {count} пользователей с offset= {offset}")
#     params = {'group_id': 'vk', 'v': 5.95, 'access_token': token, 'count': count, 'offset': offset}
#     response = requests.get(url, params=params)
#     data = response.json()
#     user_ids += data['response']['items']
#     offset += count
    
# print(user_ids)

token = '88ee22d188ee22d188ee22d11b889409c3888ee88ee22d1e9740b58eed7b187946a256b'
url = 'https://api.vk.com/method/groups.getMembers'

# count = 1000
# offset = 0
# user_ids = []

# while offset < 5000:
#     params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
#     response = requests.get(url, params=params)
#     data = response.json()
#     user_ids += data['response']['items']
#     offset += count
#     print('Ожидаю 0.5 секунды...') 
#     time.sleep(0.5)
    
# print('Цикл завершен, offset =',offset) 


# token = '88ee22d188ee22d188ee22d11b889409c3888ee88ee22d1e9740b58eed7b187946a256b'
# url = 'https://api.vk.com/method/wall.get'

# params = {'domain': 'vk', 'filter': 'owner', 'count': 1000, 'offset': 0, 'access_token': token, 'v': 5.95}

# response = requests.get(url, params=params)
# #pprint(response.json())

# stats = {}
# count_posts = 0
# for record in response.json()['response']['items'][:]:
#     title = record['text'][:30]
#     if title:
#         stats[title] = [record['comments']['count'], record['likes']['count'], record['reposts']['count'], record['date']]
#         count_posts += 1
#     if count_posts > 10:
#         break
    
# print(stats)

def task():
    print('Hello, I am task')
    return

schedule.every(5).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)