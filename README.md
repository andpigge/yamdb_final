# yamdb_final

![example workflow](https://github.com/andpigge/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

<a href="https://hub.docker.com/r/andpigge/api_yamdb">
   <li>Ссылка на образ api_yamdb в docker hub:</li>
</a>

<a href="http://178.154.221.59:3000/api/v1/titles/">
   <li>Ссылка на проект в яндекс облаке:</li>
</a>

<br/>
<a href="https://hub.docker.com/r/andpigge/api_yamdb"><img height="40px" src="https://www.unixtutorial.ru/images/software/docker-hub.png"></a>
<a href="http://178.154.221.59:3000/api/v1/titles/"><img height="40px" src="https://storage.yandexcloud.net/cloud-www-assets/region-assets/ru/light/desktop/logo.svg"></a>

<h2 align="center">Описание</h2>

Сборка готового командного проекта YaMDb с помощью docker.<br/>
<a href="https://github.com/Rejden2000/api_yamdb">
  Ссылка на командный проект YaMDb.
</a>

<p>Образ App залит на docker hub и переименован как api_yamdb. Ссылка выше &#9757;.</p>

<strong>Использовался docker compose для построения трех образов. Версия Docker 3.8 :</strong>
<li><em>Postgres</em>. Использованный образ - postgres : 13.0-alpine;</li>
<li><em>App</em>. Использованный образ - python : 3.7-slim;</li>
<li><em>Nginx</em>. Использованный образ - nginx : 1.21.3-alpine;</li>

<h2 align="center">Как запустить:</h2>

&#707;&#707; git clone git@github.com:andpigge/infra_sp2.git - клонировать репозиторий

&#707;&#707; cd infra - зайти в папку для запуска docker compose

&#707;&#707; docker-compose up -d - <em>запустить docker compose</em>

&#8212; Перейти в браузер по адресу: http://localhost/api/v1/titles/.
Подробнее: 
<a href="https://github.com/Rejden2000/api_yamdb">
  Ссылка на командный проект YaMDb.
</a>

&#707;&#707; docker-compose down - остановить и удалить контейнеры

Другие команды:<br/>
&#707;&#707; docker pull andpigge/api_yamdb - <em>забрать репозиторий</em>
