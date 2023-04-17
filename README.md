## Проект "API для Yatube"
Проект представляет собой API, предназначенный для взаимодействия бэкенда и фронтенда проекта Yatube.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone https://github.com/DaniilFedotov/api_final_yatube.git
```

```sh
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python3 manage.py migrate
```

Запустить проект:

```sh
python3 manage.py runserver
```

### Доступные эндпоинты:

* Получение публикаций

```
/api/v1/posts/
```

* Получение публикации по id

```
/api/v1/posts/{id}/
```

* Получение всех комментариев к публикации

```
/api/v1/posts/{post_id}/comments/
```

* Получения комментария к публикации по id

```
/api/v1/posts/{post_id}/comments/{id}/
```

* Получение списка доступных сообществ

```
/api/v1/groups/
```

* Получение информации о сообществе по id

```
/api/v1/groups/{id}/
```

* Возвращает все подписки пользователя, сделавшего запрос

```
/api/v1/follow/
```
