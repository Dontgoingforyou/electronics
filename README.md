# Electronics Network API

#### Это веб-приложение для управления сетью поставок электроники. Оно предоставляет API для управления данными о звеньях сети, поставщиках и других связанных объектах.

## Стек технологий
- **Backend:** Django, Django REST Framework
- **База данных:** PostgreSQL
- **Тестирование:** Unittest


## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Dontgoingforyou/electronics.git
cd electronics
```

### 2. Настройка окружения
Перед тем как собрать контейнер, переименуйте файл .env.sample в .env 

### 3. Собрать контейнер Docker(Миграции и фикстуры будут загружены автоматически, код описан в docker/entrypoint.sh)
```bash
docker compose up --build
```

### 4. Доступ к серверу

- API будет доступно по адресу [http://localhost:8000/electronics/](http://localhost:8000/electronics/)
- Swagger документация доступна по адресу [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- ReDoc документация доступна по адресу [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

### 5. Тесты
Чтобы запустить тесты, выполните команду:
```bash
docker compose exec app python manage.py test
```