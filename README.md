# RCloud
Программа предполагает, что будет переноситься на флешке, чтобы с разных компьютеров загружать файлы на Яндекс Диск пользователя. Создана, что бы пользователю не приходилось логиниться Яндексе каждый раз на разных компьютерах.

Откройте файл config.txt
- в поле 'token=your_token' введите токен, который нужно получить через Yandex OAuth
- в поле 'folder=./your_folder' введите имя папки на Яндекс диске, с которой будет работать программа
- при скачивании файлов, если указать пустой путь, они будут сохранены в папке downloads в корневой папке программы
- в текущей версии программа не запустится, если указать не верный токен
