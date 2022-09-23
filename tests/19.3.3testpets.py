import requests

headers = {'email': 'provokatorx3@gmail.com', 'password': 'qwertyu',
           'auth_key': '5b75db1e1edf3b96b0926105731ecd60cc6e0a4fdc9eb144ba2f1fe7'}

data = {
    "age": 33,
    "animal_type": "vata",
    "created_at": "1587707210.3641336",
    "id": "9C4AEC87-37A4-4EE0-8F1B-3170C816536C",
    "name": "vlata",
    "pet_photo": "",
    "user_id": "5b75db1e1edf3b96b0926105731ecd60cc6e0a4fdc9eb144ba2f1fe7"
}

data2 = {
    "age": 33,
    "animal_type": "vatavatavatavatavatavata",
    "created_at": "1587707210.3641336",
    "id": "9C4AEC87-37A4-4EE0-8F1B-3170C816536C",
    "name": "vlata",
    "pet_photo": "",
    "user_id": "5b75db1e1edf3b96b0926105731ecd60cc6e0a4fdc9eb144ba2f1fe7"
}

res = requests.get(f'https://petfriends.skillfactory.ru/api/key', headers=headers)
print(res.text)

res = requests.post(f'https://petfriends.skillfactory.ru//api/create_pet_simple', headers=headers, data=data)
print(res.text)

res = requests.get(f'https://petfriends.skillfactory.ru/api/pets?filter=my_pets', headers=headers)
print(res.text)

res = requests.put(f'https://petfriends.skillfactory.ru//api/pets/4532d9e8-12dd-48a4-a670-409fd8a028ab',
                   headers=headers, data=data2)
print(res.text)

res = requests.delete(f'https://petfriends.skillfactory.ru//api/pets/4532d9e8-12dd-48a4-a670-409fd8a028ab',
                      headers=headers)
print(res.text)
