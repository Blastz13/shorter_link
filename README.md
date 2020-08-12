# Установка и настройка

**Установка**

Вы можете склонировать данное приложение:

```bash
git clone https://github.com/Blastz13/shorter_link.git
```

Далее, нужно установить нужные библиотеки

```bash
pip3 install -r requirements.txt
```

**Настройка**

Перейдите в каталог веб-приложения, создайте миграции и соберите статику.

```bash
cd tree_emploes
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```

Также, вы можете создать супер-юзера. Это делается с помощью команды:

```bash
python3 manage.py createsuperuser
```

Теперь вы можете запускать сервер.

```bash
python3 manage.py runserver
```

Теперь вы успешно можете пользоваться 


### Лицензия

Copyright © 2020 [Blastz13](https://github.com/Blastz13/). 
