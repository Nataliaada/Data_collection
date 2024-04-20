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
        with open("fifa_rankings.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            # Извлечение заголовков столбцов таблицы
            headers = [th.text_content().strip() for th in table.xpath('.//thead')]
            writer.writerow(headers)

            # Извлечение данных из таблицы и запись в CSV-файл
            rows = table.xpath('.//tbody/tr') 
            for row in rows:
                 data = [td.text_content().strip() for td in row.xpath('.//td')]
                 writer.writerow(data)
        print(rows)
        print("Данные успешно извлечены и сохранены в fifa_rankings.csv")

    except requests.exceptions.RequestException as e:
        print("Ошибка при отправке запроса:", e)
    except IndexError:
        print("Не удалось найти таблицу на странице.")
    except Exception as e:
        print("Произошла ошибка:", e)

# Вызов функции для скрапинга данных
scrape_fifa_rankings()
