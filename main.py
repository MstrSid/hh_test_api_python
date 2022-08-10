import requests


def get_info(url):
    r = requests.get(url)
    j = r.json()
    return j['items']


res = get_info("https://api.hh.ru/vacancies?professional_role=96")

for val in res:
    print(f'{val["name"]}\n{val["address"]["city"] if val["address"] is not None else "no data"}\n')
