# Тесты для Auth API

import requests

from conftest import my_test_user
from constants import BASE_URL_AUTH, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT


class TestAuthAPI:

    def test_register_user(self, my_test_user):
        # URL для регистрации
        register_url = f"{BASE_URL_AUTH}{REGISTER_ENDPOINT}"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=my_test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == my_test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_authorized_my_test_user(self, my_test_user):
        # URL для авторизации
        authorized_url = f"{BASE_URL_AUTH}{LOGIN_ENDPOINT}"

        data = {
            "email": my_test_user["email"],
            "password": my_test_user["password"]
        }

        response = requests.post(authorized_url, json=data, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 200, "Ошибка авторизации пользователя!"
        response_data = response.json()
        assert response_data["user"]["fullName"] == my_test_user["fullName"], "Имена не совпадает"
        assert response_data["user"]["email"] == my_test_user["email"], "Email не совпадают."

        # Проверяем, что роль USER назначена по умолчанию
        assert response_data["user"]["roles"] == my_test_user["roles"], "Роли не совпадают."

        # Проверяем что сервер выдал токены
        assert response_data["accessToken"] is not None, "Сервер не выдал accessToken"
        assert response_data["refreshToken"] is not None, "Сервер не выдал refreshToken"


