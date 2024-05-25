import requests
from bs4 import BeautifulSoup as b

url = 'https://culturazdoroviya.ru/tablicy/tablica-kaloriynosti-produktov.html'
async def parser(url):
        r = requests.get(url)
        soup = b(r.text, 'html.parser')
        dots = soup.find_all('table')
        
        return dots

async def search_product(number):
    print(number)
    dots = await parser(url)
    table_dots = dots[number].find_all('tr')
    list_dot = []
    for i in table_dots:
        element_table = i.find_all('td')
        list_dot.append({
            'name': element_table[0].text,
            'belki': element_table[1].text,
            'jir': element_table[2].text,
            'ugl': element_table[3].text,
            'calories': element_table[4].text
        })
    del list_dot[0]
    return list_dot
    
