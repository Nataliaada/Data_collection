import requests
from lxml import html
import csv

def scrape_fifa_rankings():
    # URL страницы с рейтингами FIFA
    url = "https://www.fifa.com/fifa-world-ranking/"

    # Заголовок HTTP-запроса с пользовательским агентом
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # Отправка GET-запроса и получение HTML-содержимого страницы
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка наличия ошибок

        # Создание объекта парсера
        parser = html.fromstring(response.text)

        # Выражение XPath для выбора таблицы с рейтингом
        table_xpath = '//table'
        table = parser.xpath(table_xpath)[0]
     
  

        # Создание CSV-файла для сохранения данных
        with open("fifa_rankings.csv1", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

           # Извлечение названий столбцов
            headers = [th.text_content().strip() for th in table.xpath('.//thead/tr/th')]
            writer = csv.DictWriter(csvfile, fieldnames = headers) 
# Извлечение данных из таблицы и преобразование их в словарь
            rows = table.xpath('.//tbody/tr')  # Пропускаем заголовок таблицы
            print(rows)
            data = []
            for row in rows:  
                first_element = row.xpath('.//td/div/span')[0].text_content()  # Извлечение первого элемента строки
                data.append({
                    headers[0]: first_element,  # Добавление первого элемента в словарь с ключом из первого столбца
                    headers[1]: row.xpath('.//td')[1].text_content(),  # Добавление второго элемента в словарь с ключом из второго столбца
                    headers[2]: row.xpath('.//td')[2].text_content(),  # Добавление третьего элемента в словарь с ключом из третьего столбца
                    headers[3]: row.xpath('.//td')[3].text_content(),  # Добавление четвертого элемента в словарь с ключом из четвертого столбца
                })
            writer.writeheader() 
            writer.writerows(data)          
              
# Вывод словаря
        print(data)     
      
    except requests.exceptions.RequestException as e:
        print("Ошибка при отправке запроса:", e)
    except IndexError:
        print("Не удалось найти таблицу на странице.")
    except Exception as e:
        print("Произошла ошибка:", e)

# Вызов функции для скрапинга данных
scrape_fifa_rankings()







