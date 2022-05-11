
<p align="center">
  <img src="https://img.shields.io/badge/Platform-Telegram-blue" >
</p>

# Telegram password manager bot

Бот разработан в обучающих целях и не рекоммендован для хранения настоящих данных.

<img src="images/hello.jpg" alt=''>

## Функционал бота

|                |                             |
| -------------  | --------------------------- |
| Поиск          | Добавление аккаунта         |
| Редактирование | Формирование таблицы данных |
| Удаление       | Генерация пароля            |  

Для управления используются inline-кнопки. Все пароли и данные пользователя хранятся в таблицах SQLite. Написан на python с исспользованием библиотеки aiogram.
<p>
    <img src="images/one.jpg" alt='' width="25%" height="25%">
    <img src="images/three.jpg" alt='' width="25%" height="25%">
    <img src="images/two.jpg" alt='' width="25%" height="25%">
</p>

## Демонстрация

<p>
    <img src="" alt='' align="center">
    <br>Основное меню
</p>

<p>
    <img src="" alt='' align="center">
    <br>Генерация таблицы данных
</p>

## Тест-драйв

Можете скачать и протестировать работу. Для этого измените данные в <b>data/config.ini</b>

```bash
{
    "token": "TOKEN",
    "admins": "id_1 id__2 id_3"
}
```


## Файлы для деплоя
При тестировании необходимо обновить runtime.txt до последней версии [python](https://www.python.org/).
 - [Все зависимости лежат тут](https://github.com/jonotyan/telegram-password-manager/blob/main/requirements.txt)
 - [Procfile](https://github.com/jonotyan/telegram-password-manager/blob/main/Procfile)
 - [Runtime](https://github.com/jonotyan/telegram-password-manager/blob/main/runtime.txt)


## Автор

- [@jonotyan](https://www.github.com/jonotyan)

