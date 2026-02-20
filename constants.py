# Глобальные константы

BASE_URL_MOVIES = "https://api.dev-cinescope.coconutqa.ru" # базовый url для фильмов
MOVIES_ENDPOINT = "/movies" # фильмы
GENRES_ENDPOINT = "/genres" # жанры

BASE_URL_AUTH = "https://auth.dev-cinescope.coconutqa.ru" # авторизация базовый url
LOGIN_ENDPOINT = "/login"
REGISTER_ENDPOINT = "/register"

BASE_URL_PYMENT = "https://payment.dev-cinescope.coconutqa.ru" # оплата

# Заголовки для запросов
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Креды админа (имеет все роли)
ADMIN_CRED = {
    "username": "api1@gmail.com",
    "password": "asdqwe123Q"
}