# yamdb_final

![example workflow](https://github.com/andpigge/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

<h2 align="center">Технологии</h2>

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

<a href="https://hub.docker.com/r/andpigge/api_yamdb"><img height="30px" src="https://www.unixtutorial.ru/images/software/docker-hub.png"></a>
<a href="http://178.154.221.59:3000/api/v1/titles/"><img height="30px" src="https://storage.yandexcloud.net/cloud-www-assets/region-assets/ru/light/desktop/logo.svg"></a>

<h2 align="center">Описание</h2>

<h6>Порты 80 и 443 на сервере зяняты проектом <a href='https://github.com/andpigge/api_final_yatube'>api_final_yatube</a></h6>

Api для различных произведений, комментарий и отзывы к ним.

Реализована своя систему прав доступа. Регистрация и получения токена по коду из почты.

Настроен импорт данных из .csv, exell формат, напрямую в базу данных.

Основная задача для этого репозитория заключалась в настройке задач CI/CD для готового командного проекта:<br/>
<a href="https://github.com/Rejden2000/api_yamdb">
  Ссылка на командный проект YaMDb.
</a>
<ol>&#9679;&nbsp;&nbsp; проверка на flake8 и прогон заранее предоставленных тестов,</ol>

<ol>&#9679;&nbsp;&nbsp; сборка готового командного проекта YaMDb с помощью docker compose и загрузка образов на docker hub,<br/>
<ins><a href="https://hub.docker.com/r/andpigge/api_yamdb">
   Ссылка на образы api_yamdb в docker hub.
</a><p></p></ol></ins>

<ol>&#9679;&nbsp;&nbsp; билд на сервер яндекс облако из образов docker hub,<br/>
<ins><a href="http://178.154.221.59:3000/api/v1/titles/">
   Ссылка на проект в яндекс облаке.
</a><p></p></ol></ins>

<strong>Использовался docker compose для построения трех образов. Версия Docker 3.8 :</strong>
<ol><em>&#8212;&nbsp;&nbsp; Postgres</em>. Использованный образ - postgres : 13.0-alpine;</ol>
<ol><em>&#8212;&nbsp;&nbsp; App</em>. Использованный образ - python : 3.7-slim;</ol>
<ol><em>&#8212;&nbsp;&nbsp; Nginx</em>. Использованный образ - nginx : 1.21.3-alpine;</ol>

<h2 align="center">О командном проекте YaMDb:</h2>

<h3><li><a href='https://github.com/Rejden2000/api_yamdb#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C'>установка проекта YaMDb без docker;</a></li></h3>
<h3><li><a href='https://github.com/Rejden2000/api_yamdb#%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9'>примеры api;</a></li></h3>
<h3><li><a href='https://github.com/Rejden2000/api_yamdb#%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9'>технологии;</a></li></h3>
<h3><li><a href='https://github.com/Rejden2000/api_yamdb#%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9'>авторы;</a></li></h3>

<h2 align="center">Процесс развертывания docker compose:</h2>

Убедитесь что на вашем компьтере установлен docker и docker compose:
```
docker version
```
```
docker-compose --version
```

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:andpigge/yamdb_final.git
```
```
cd yamdb_final
```

Зайти в папку infra для запуска docker compose и запустить docker compose из этой папки:
```
cd infra
```
```
docker-compose up -d
```

Docker-compose развернут. Перейдите в браузер по адресу для просмотра проекта:
```
http://localhost/api/v1/titles/
```

Остановить и удалить контейнеры. Запустите команду в папке
```
docker-compose down
```

Другие команды.

Скачать образ из docker hub:
```
docker pull andpigge/api_yamdb
```
