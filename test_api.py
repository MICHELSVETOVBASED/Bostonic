import requests
import json


# Тест создания продукта
def test_create_product():
    url = "http://127.0.0.1:8000/api/v1/products/"
    data = {"name": "Test Product", "description": "Test Description", "price": 100}

    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code == 200:
            print("✅ Продукт успешно создан!")
        else:
            print("❌ Ошибка при создании продукта")

    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")


if __name__ == "__main__":
    test_create_product()
