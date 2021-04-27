import requests
from bs4 import BeautifulSoup
import json

link = 'https://azan.ru/kutub/view/asharityi-ahlyu-s-sunna-val-dzhamaa-318'
links_of_categories = []
r = requests.get(url=link)
soup = BeautifulSoup(r.text, 'lxml')
categories = soup.find('div', class_='multimedia-categories multimedia-categories_trands '
                                     'multimedia-categories_books card')
header = categories.find('div', class_='multimedia-categories__title')
items = categories.find_all('a')
# for item in items:
#     links_of_categories.append('https://azan.ru'+item.get('href'))
headers = ['Коран и его тафсиры', 'Акыда (Вероубеждение)', 'Дауат - призыв', 'Фикх (Исламское право)', 'Фетвы',
           'Хадисы', 'Жизнеописание Пророка', 'История Пророков', 'Благородные сподвижники', 'История Ислама',
           'Биография учёных', 'Адаб (этика) и суфизм', 'Мудрость и наставления', 'Обучающая литература',
           'Оберегание человека', 'Поминания Аллаха', 'Дозволенное и запретное', 'Течения и секты', 'Апологетика',
           'Для сестер', 'Семья в Исламе', 'Книги для детей', 'Медицина', 'Исламские финансы', 'Прочее']


# get all book links from category
def get_all_links(url) -> dict:
    dict_of_link = {}
    for x in range(1, 8):
        re = requests.get(url=f'{url}?page={x}')
        if r.status_code == 200:
            soups = BeautifulSoup(re.text, 'lxml')
            try:
                card_document = soups.find('div', class_='books-on-subject card document')
            except SyntaxError:
                continue
            try:
                books = card_document.find_all('a', class_='books-on-subject__image-link')
                for book in books:
                    # link_list.append('https://azan.ru' + book.get('href'))
                    dict_of_link.update({
                        book.find('img').get('alt'): 'https://azan.ru' + book.get('href')
                    })
            except SyntaxError:
                continue

    return dict_of_link


urls = ['https://azan.ru/maktabah/kutub/Koran-i-ego-tafsiryi',
        'https://azan.ru/maktabah/kutub/akyida-veroubezhdenie', 'https://azan.ru/maktabah/kutub/dauat-prizyiv',
        'https://azan.ru/maktabah/kutub/fikh-Islamskoe-pravo', 'https://azan.ru/maktabah/kutub/fetvyi',
        'https://azan.ru/maktabah/kutub/hadisyi',
        'https://azan.ru/maktabah/kutub/zhizneopisanie-proroka', 'https://azan.ru/maktabah/kutub/istoriya-prorokov',
        'https://azan.ru/maktabah/kutub/blagorodnyie-spodvizhniki', 'https://azan.ru/maktabah/kutub/istoriya-Islama',
        'https://azan.ru/maktabah/kutub/biografiya-uchyonyih', 'https://azan.ru/maktabah/kutub/adab-etika-i-sufizm',
        'https://azan.ru/maktabah/kutub/mudrost-i-nastavleniya',
        'https://azan.ru/maktabah/kutub/obuchayuschaya-literatura',
        'https://azan.ru/maktabah/kutub/obereganie-cheloveka',
        'https://azan.ru/maktabah/kutub/pominaniya-Allaha', 'https://azan.ru/maktabah/kutub/dozvolennoe-i-zapretnoe',
        'https://azan.ru/maktabah/kutub/techeniya-i-sektyi', 'https://azan.ru/maktabah/kutub/apologetika',
        'https://azan.ru/maktabah/kutub/dlya-sester', 'https://azan.ru/maktabah/kutub/semya-v-Islame',
        'https://azan.ru/maktabah/kutub/knigi-dlya-detey', 'https://azan.ru/maktabah/kutub/meditsina',
        'https://azan.ru/maktabah/kutub/Islamskie-finansyi', 'https://azan.ru/maktabah/kutub/prochee']

with open('D:\Pycharm projects\/aio_names_bot\data\/books_url.json', 'w', encoding='utf-8') as file:
    data = {}
    for a, b in zip(headers, urls):
        data.update({
            a: get_all_links(b)
        })
    json.dump(data, file, indent=2, ensure_ascii=False)
