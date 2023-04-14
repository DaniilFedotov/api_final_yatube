## Проект "API для Yatube"
Проект представляет собой API, предназначенный для взаимодействия бэкенда и фронтенда проекта Yatube.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DaniilFedotov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
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