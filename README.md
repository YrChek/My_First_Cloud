# My_First_Cloud

Мой дипломный проект

## Структура проекта

My_First_Cloud  
&ensp; |&mdash; &mdash; app \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; migrations \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; \_init\_.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; admin.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; apps.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; models.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; paginator.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; serializer.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; views.py \
&ensp; | \
&ensp; |&mdash; &mdash; files \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; img \
&ensp; | \
&ensp; |&mdash; &mdash; frontend \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; build \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; static \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; index.html \
&ensp; | \
&ensp; |&mdash; &mdash; my_first_cloud \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; \_init\_.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; asgi.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; settings.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; urls.py \
&ensp; |&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&mdash; &mdash; wsgi.py \
&ensp; | \
&ensp; |&mdash; &mdash; manage.py \
&ensp; |&mdash; &mdash; requirements.txt

**My_First_Cloud** - это корневой каталог проекта

**app** - Django приложение, где содержатся:

* python пакет **migrations** с записями всех изменений, внесенных в базу данных;
* **_ init _.py** - пустой файл Python, который сообщает интерпретатору Python, что каталог **app** является пакетом Python;
* **admin.py** - регистрация модели User в администрации Django;
* **apps.py** - это общий файл конфигурации для всех приложений Django. Конфигурации оставлены по умолчанию;
* **models.py** - модуль, где созданы модели (таблицы) для базы данных;
* **paginator.py** - модуль с классом пагинатора, для выдачи записей из базы данных постранично, с ограничением по количеству выдаваемых записей за один раз;
* **serializer.py** - модуль с сериализаторами для сериализации, десериализации и валидации данных, необходимых для записи, изменения или получения данных из базы данных;
* **views.py** - модуль с представлениями. Предоставляет интерфейс, через который пользователи взаимодействуют с веб-сайтом.

**files** - каталог, где хранятся изображения, используемые в проекте и где будут хранится файлы, загруженные пользователями.

**frontend** - каталог, где хранятся html, js и css файлы, сгенерированные для релизной сборки.

**my_first_cloud**  - это фактический каталог проекта, содержащий:

* **_ init _.py** - пустой файл Python, который сообщает интерпретатору Python, что каталог **my_first_cloud** является пакетом Python;
* **asgi.py** - интерфейс шлюза асинхронного сервера;
* **settings.py** - основной файл конфигурации проекта;
* **urls.py** - содержит конфигурацию url-адресов для приложения;
* **wsgi.py** - интерфейс шлюза веб-сервера.

**manage.py** - утилита командной строки для проекта Django;

**requirements.txt** - список внешних зависимостей.

## Развертывание проекта на REG.RU

#### Создание сервера

1. [Заходим на сайт Reg.ru](https://www.reg.ru/).

1. Проходим процедуру регистрацию (если регистрация отсутствует).
1. Заходим в личный кабинет. В главном меню выбираем рег.облако.
1. Если заказываем сервер впервые, то нажимаем "Запустить первый север", иначе нажимаем "Новый ресурс" &ensp;  -> &ensp; "Создать новый сервер".
1. Выбираем регион размещения.
1. В "Образы" выбираем операционную систему "Ubuntu".
1. Выбираем тарифный план.
1. Создаем и добавляем ssh-ключ (по-желанию).
1. Можно сменить название сервера.
1. Нажимаем "Заказать сервер" и ждем создания. Когда сервер создастся, на зарегистрированную почту придет письмо с адресом сервера, логином и паролем.

#### Подготовка сервера

1. Подключаемся к серверу через ssh-ключ со своего компьютера

       ssh [логин из письма на почту]@[ip-адрес, из письма почту]

      либо через консоль на сайте, введя логин из почты.

1. Вводим требуемые пароли.
1. Создадим нового пользователя (user_name):

       adduser [имя нового пользователя]
1. Добавим нового пользователя в группы sudo и www-data:

       usermod user_name -aG sudo
       usermod user_name -aG www-data
1. Переключимся на нового пользователя:

        su user_name
1. Перейдем в папку нового пользователя:

       cd ~
1. Проверим, что python и git установлены:

       python3 --version
       git --version
1. Обновим список доступных репозиториев для пакетного менеджера:

       sudo apt update
1. Установим виртуальное окружение, pip, postgresql, nginx:

        sudo apt install python3-venv python3-pip postgresql nginx

#### Установка базы данных

1. Переключимся на юзера postgres:

       sudo su postgres
1. Зайдем в postgresql:

       psql
1. Зададим пароль пользователю postgres:

        ALTER USER postgres WITH PASSWORD '[пароль]';
1. Создадим базу данных:

        CREATE DATABASE [название базы данных];
1. Выходим из БД:

        \q
1. Выходим из пользователя postgres:

        exit

#### Клонирование проекта

1. Клонируем проект:

        git clone [https ссылка репозитория]
1. Заходим в папку нашего проекта:

        cd My_First_Cloud
1. Cоздадим файл .env и пропишем там нужные значения настройки:

        nano .env

    ```
    SECRET_KEY=[секретный ключ Django]
    DEBUG=False
    ALLOWED_HOSTS=[используемые IP-адреса]
    DB_NAME=[название базы данных]
    DB_USER=postgres
    DB_PASSWORD=[пароль базы данных]
    DB_HOST=localhost
    DB_PORT=5432
    ```

   сохраняем (ctrl + S), выходим из файла (ctrl + X)
1. Создадим виртуальное окружение:

        python3 -m venv env
1. Активируем виртуальное окружение:

        source env/bin/activate
1. Установим модули из файла requirements.txt:

        pip install -r requirement.txt
1. Применим миграции:

        python manage.py migrate
1. Создадим суперпользователя:

        python manage.py createsuperuser
1. Соберем статику:

        python manage.py collectstatic
1. Выйдем из виртуального окружения:

        deactivate

#### Развертывание проекта

1. Создадим файл с настройками gunicorn.service.

        sudo nano /etc/systemd/system/gunicorn.service

    ```
    [Unit]
    Description=gunicorn service
    After=network.target

    [Service]
    User=[имя пользователя]
    Group=www-data
    WorkingDirectory=/home/[имя пользователя]/My_First_Cloud
    ExecStart=/home/[имя пользователя]/My_First_Cloud/env/bin/gunicorn --access-logfile - --workers=2 \
              --bind unix:/home/[имя пользователя]/My_First_Cloud/my_first_cloud/project.sock my_first_cloud.wsgi:application

    [Install]
    WantedBy=multi-user.target
    ```

    сохраняем (ctrl + S), выходим из файла (ctrl + X)
1. Активируем кофигурацию gunicorn и запускаем процесс:

        sudo systemctl enable gunicorn
        sudo systemctl start gunicorn
1. Создадим файл с настройками nginx:

        sudo nano /etc/nginx/sites-available/cloud_project

    ```
    server {
      listen 80;
      server_name [IP-адрес];

      location /static/ {
        root /home/[имя пользователя]/My_First_Cloud;
      }

      location /files/ {
        root /home/[имя пользователя]/My_First_Cloud;
      }

      location / {
        include proxy_params;
        proxy_pass http://unix:/home/[имя пользователя]/My_First_Cloud/my_first_cloud/project.sock;
      }
    }
    ```
1. Внесем измененя в файл nginx.conf:

        sudo nano /etc/nginx/nginx.conf
   Вместо **user www-data;** пропишем **user [имя пользователя] www-data;**
1. При помощи фаервола, нужно дать полные права nginx:

        sudo ufw allow 'Nginx Full'
1. Создаем символическую ссылку:

        sudo ln -s /etc/nginx/sites-available/cloud_project /etc/nginx/sites-enabled/cloud_project
1. Перезапускаем NGINX:

        sudo systemctl stop nginx
        sudo systemctl start nginx

Теперь, перейдя по IP-адресу в браузере, увидим свой проект.
