# Проект Wiki на Flask

## Описание проекта

Этот проект будет интересен тем кому под рукой нужен удобный wiki.

## Возможности проекта

* Собственная локальная база данных(не требуется установка локального веб-сервера)
* Каждые 10 минут выполняется дамп базы данных и выгрузка разделов в excel 
* С помощью специально написанных скриптов bash и powershell, приложение можно запускать и перезапускать на локальной машине


## Требования к программному обеспечению

* Установлен Python
* Установлен Git

## Установка проекта

1. Открываем любой CLI
2. Вводим команду 
```
git clone https://github.com/savinsyu/flask-project.git
```
3. Переходим в папку flask-project 
4. Запускаем скрипт start_app.sh
5. В браузере откроеткся страница приложения


## Описание файлов корневой директории

# requirements.txt

Файл со списком зависимостей приложения

# reboot_app.sh
# database.db
# dbackup.db

# dkill_python.ps1
# dstart_app.sh
# dapp.py

# ddump_export_every.sh
# dapp.sh
# dhotfix.sh

# drealese.sh