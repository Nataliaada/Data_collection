Курс "Сбор и разметка данных" от GeekBrains образца 2024 года

## Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
Решение задачи 1 для Озон (скриншот)

Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
Решение задачи 2 - запрос по автору через API сервиса Open Library

Решение задачи 2 - запрос по названию книги через API сервиса Open Library

Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
Решение задач 3 - 7

## Урок 2. Парсинг HTML. BeautifulSoup
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Затем сохранить эту информацию в JSON-файле.

## Урок 3. Системы управления базами данных MongoDB и Кликхаус в Python
Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass


Решение задачи 1 - проведенная регистрация в облачном сервисе MongoDB - скриншот

Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
Поэкспериментируйте с различными методами запросов.
Решение задач 3 - 4 - код в файле .ipynb

Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения.
Решение задач 5 - 6 - скриншот

Вывод о решении задач 5 - 6: загеристрироваться в ClickHouse получилось, но сервис не выдает API keys для доступа к облачному хранилищу из-за политики ограничений для России, поэтому загрузить данные в облачное хранилище невозможно.


## Урок 4. Парсинг HTML. XPath
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.

## Урок 6. Scrapy. Парсинг фото и файлов
Домашнее задание
1. Создайте новый проект Scrapy. Дайте ему подходящее имя и убедитесь, что ваше окружение правильно настроено для работы с проектом.

2. Создайте нового паука, способного перемещаться по сайту www.unsplash.com. Ваш паук должен уметь перемещаться по категориям фотографий и получать доступ к страницам отдельных фотографий.

3. Определите элемент (Item) в Scrapy, который будет представлять изображение. Ваш элемент должен включать такие детали, как URL изображения, название изображения и категорию, к которой оно принадлежит.

4. Используйте Scrapy ImagesPipeline для загрузки изображений. Обязательно установите параметр IMAGES_STORE в файле settings.py. Убедитесь, что ваш паук правильно выдает элементы изображений, которые может обработать ImagesPipeline.

5. Сохраните дополнительные сведения об изображениях (название, категория) в CSV-файле. Каждая строка должна соответствовать одному изображению и содержать URL изображения, локальный путь к файлу (после загрузки), название и категорию


