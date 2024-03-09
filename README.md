# YaCut - Сервис Укорачивания Ссылок

Добро пожаловать в YaCut - ваш персональный сервис укорачивания ссылок! С этим инструментом вы можете легко создавать короткие идентификаторы для ваших длинных ссылок, делая их более удобными для обмена.
## Возможности: 

1. Генерация коротких ссылок: Воспользуйтесь нашей удобной формой для создания коротких идентификаторов для ваших длинных ссылок.
2. Переадресация: При обращении к коротким ссылкам происходит автоматическая переадресация на исходный адрес.

## Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/OFF1GHT/yacut.git
```

```
cd yacut
```

## Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

## Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Создайте файл .env:

```
FLASK_APP=yacut/__init__.py
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

## Создайте базу данных и применить миграции:
```
flask db init
```
```
flask db migrate
```
```
flask db migrate
```