# openphish_data_parser
Домашнее задание по предмету "Применение ML в кибербезопасности" (ВШЭ МИЕМ)

## Начало работы

- Склонируйте репозиторий:
```
git clone git@github.com:monticola145/openphish_data_parser.git
```
- Создайте и разверните виртуальное окружение
```
python -m venv venv && source venv/Scripts/activate
```
- Установите зависимости
```
pip install -r requirements.txt
```
- Запустите приложение
```
python main.py
```

## Принцип работы

Программа выполняет следующие функции:

- Каждые 5 минут программа парсит информацию с сайта OpenPhish
- Проверяет на уже существующие записи в CSV файле, отсеивает дубликаты, новые данные записывает в файл
- Через час (или после 12-ой итерации) подводит итоги, выводя в консоль информацию о начале и конце парсинга, количество уникальных URL, топ 3 самых атакуемых сайта

### Автор:

[Monticola]
Git - https://github.com/monticola
Email - ```jandiev2001@yandex.ru```


# openphish_data_parser
Homework on "ML Applications in Cybersecurity" (HSE MIEM)

## Getting Started

- Clone the repository:
```
git clone git@github.com:monticola145/openphish_data_parser.git
```
- Create and deploy a virtual environment
```
python -m venv venv && source venv/Scripts/activate
```
- Install the dependencies
```
pip install -r requirements.txt
```
- Run the application
```
python main.py
```

## Principle of operation

The program performs the following functions:

- Every 5 minutes the program parses information from the OpenPhish site
- Checks for already existing entries in the CSV file, sifts out duplicates, and writes new data to the file
- After one hour (or after the 12th iteration) summarizes, displaying in the console information about the beginning and end of parsing, the number of unique URLs, the top 3 most attacked sites

### Author:

[Monticola]
Git - https://github.com/monticola
Email - ``jandiev2001@yandex.ru``
