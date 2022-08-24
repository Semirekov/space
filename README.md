# space
- Набор скриптов для загрузки из различных источников фотографий на космическую тематику.
- Бот для загрузки фотографий в телеграм-канал.

## Цель проекта
Автоматизировать процесс пополнения контента в телеграм-канале.

## Как установить
Python должен быть уже установлен.
Для установки зависимостей воспользуйтесь командой 'pip' или 'pip3'.

```
  pip install -r requirements.txt
```

Получите токены [NASA](https://api.nasa.gov/) и [Telegram](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html), сохраните их в файле .env вместе с "chat_id" телеграм-канала

```
NASA_TOKEN=<YOUR_NASA_TOKEN>
TELEGRAM_TOKEN=<YOUR_TELEGRAM_TOKEN>
TELEGRAM_CHAT_ID=<YUOR_CHAT_ID> #Example – @spacefanat
```

При желании можно в этом же файле задать каталог в который будут сохраняться фотографии. По умолчанию — подкаталог "images".

```
TARGET_DIR=<YOUR_DIR>
```

## Как использовать

#### Последний запуск в SpaceX
```
  python3 fetch_spacex_last_launch.py
```

Если по последнему запуску нет фото, то можно вызвать с таким ID запуска
```
  python3 fetch_spacex_last_launch.py 5eb87d47ffd86e000604b38a
```

#### NASA APOD
Необязательный аргумент "count" — cколько нужно скачать фото. По умолчанию 50.
```
  python3 fetch_nasa_apod.py
```

#### NASA EPIC
```
  python3 fetch_nasa_epic.py
```

#### Post One image into telegram channel

Принимает в качестве аргумента имя файла, например:
```
  python3 bot.py 'space_000.jpg'
```

#### Uploading photos from the "images" catalog on a schedule

Необязательный аргумент "pause" в секундах. Задает периодичность загрузки. По умолчанию задано четыре часа (14 400 сек.)
```
  python3 batch_upload.py 
```
