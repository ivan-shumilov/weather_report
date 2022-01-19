# Проект на Django, который будет обращаться в сервис погоды и на главной странице будет показывать погоду в данный момент времени, каждый запрос записывать в базу, в таблице должно быть id, город, погода, время когда был сделан запрос.

В данном проекте используется база sqllite и обычное виртуально окружение (нет смысла из-за одного контейнера и простых настроек поднимать докер).

Нужно создать виртуальное окружение: virtualenv -p python3 env

Затем активировать его: source env/bin/activate

Сервис погоды: https://api.stormglass.io/v2/weather/point

Нужно зарегистрироваться на этом ресурсе и получить ключ и также надо сделать на https://ipstack.com/.

После активации окружения нужно добавить в консоль переменные:

export API_STORMGLASS_URL=https://api.stormglass.io/v2/weather/point

export API_STORMGLASS_KEY='your key'

export API_IPSTACK_URL=https://api.ipstack.com

export API_IPSTACK_KEY='your key'

## Комманда, которую надо выполнить при первой активации виртуального окружения

pip install -r requirements.txt

## Запуск проекта

python manage.py runserver
