from api import PetFriends
from settings import *
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email,
        password=valid_password):
    """ Проверяем, что запрос api-ключа возвращает статус 200,
    и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ
    # с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    print(result)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем, что запрос всех питомцев возвращает не пустой
    список. Для этого сначала получаем api-ключ и сохраняем
    в переменную auth_key. Далее, используя этот ключ, запрашиваем
    список всех питомцев и проверяем, что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо ''.      """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert result['pets']


def test_add_new_pet_with_valid_data(name='Барбоскин',
        animal_type='двортерьер',
        age='4',
        photoKey='pic1'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца
    # и сохраняем в переменную pet_photo
    pet_photo=f'images/{pet_photo_all[photoKey]}'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key,
                    name,
                    animal_type,
                    age,
                    pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем
    # нового и опять запрашиваем список своих питомцев
    if not my_pets['pets']:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем
    # запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем, что статус ответа равен 200,
    # и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик',
        animal_type='Котэ',
        age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if my_pets['pets']:
        status, result = pf.update_pet_info(
                auth_key,
                my_pets['pets'][0]['id'],
                name,
                animal_type,
                age
        )
        # Проверяем что статус ответа = 200
        # и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если список питомцев пустой, то выкидываем исключение
        # с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


    ##########################################
##################### My Tests #################
    ##########################################


def test_add_new_pet_without_photo(name='Котопёс',
            animal_type='КотПёс',
            age='100'):
    """Проверяем, что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_pet_photo(photoKey='pic2'):
    """Проверяем, что можно добавить фото питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой,
    # или у последнего в списке уже есть фотка,
    # то добавляем нового и опять запрашиваем список своих питомцев
    if not my_pets['pets'] or 'data:image/jpeg;base64' in my_pets['pets'][0]['pet_photo']:
        pf.add_new_pet_without_photo(
                auth_key,
                "СуперПуперКот",
                "котяра",
                "10"
        )
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца
    # и сохраняем в переменную pet_photo
    pet_photo=f'images/{pet_photo_all[photoKey]}'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Берём id первого питомца из списка и отправляем запрос
    # на добавление фотографии
    pet_id = my_pets['pets'][0]['id']

    # Добавляем фотографию питомца
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['id'] == pet_id



################ Negative Tests ###############


def test_get_api_key_for_invalid_userName1(
        emailKey='empty',
        password=valid_password
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода логина"""
    email = invalid_email[emailKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nЭлектронная почта:\n{emailKey}\n{email}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_userName2(
        emailKey='kirilic',
        password=valid_password
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода логина"""
    email = invalid_email[emailKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nЭлектронная почта:\n{emailKey}\n{email}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_userName3(
        emailKey='unknown',
        password=valid_password
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода логина"""
    email = invalid_email[emailKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nЭлектронная почта:\n{emailKey}\n{email}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_userName4(
        emailKey='wrong',
        password=valid_password
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода логина"""
    email = invalid_email[emailKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nЭлектронная почта:\n{emailKey}\n{email}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_password1(
        email=valid_email,
        passwordKey='empty'
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода пароля"""
    password = invalid_password[passwordKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nПароль:\n{passwordKey}\n{password}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_password2(
        email=valid_email,
        passwordKey='kirilic'
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода пароля"""
    password = invalid_password[passwordKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nПароль:\n{passwordKey}\n{password}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_password3(
        email=valid_email,
        passwordKey='special'
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода пароля"""
    password = invalid_password[passwordKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nПароль:\n{passwordKey}\n{password}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_password4(
        email=valid_email,
        passwordKey='spacesAround'
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода пароля"""
    password = invalid_password[passwordKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nПароль:\n{passwordKey}\n{password}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_get_api_key_for_invalid_password5(
        email=valid_email,
        passwordKey='special_v2'
    ):
    """ Проверяем, что запрос api-ключа возвращает статус 403:
    ошибка ввода пароля"""
    password = invalid_password[passwordKey]
    status, result = pf.get_api_key(
        email,
        password
    )
    print(f'\nПароль:\n{passwordKey}\n{password}\nПришедший response:\n{result}\n')
        # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'This user wasn&#x27;t found in database' in result


def test_add_new_pet_nameTest1(nameKey='empty',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest2(nameKey='kirilic',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest3(nameKey='special',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest4(nameKey='spacesAround',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest5(nameKey='special_v2',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest6(nameKey='long255',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest7(nameKey='long256',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest8(nameKey='long1024',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_nameTest9(nameKey='long2048',
            animal_type='Нормальный такой кот',
            age='2'):
    """Проверяем, что можно добавить питомца
    с некорректной кличкой"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    name = pet_name_type[nameKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest1(typeKey='empty',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest2(typeKey='kirilic',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest3(typeKey='special',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest4(typeKey='spacesAround',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest5(typeKey='special_v2',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest6(typeKey='long255',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest7(typeKey='long256',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest8(typeKey='long1024',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_typeTest9(typeKey='long2048',
            name='Котопёсыч',
            age='1'):
    """Проверяем, что можно добавить питомца
    с некорректным видом животного"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    animal_type = pet_name_type[typeKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest1(ageKey='empty',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest2(ageKey='negative',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest3(ageKey='zero',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest4(ageKey='text',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest5(ageKey='big',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest6(ageKey='large',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest7(ageKey='float',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_ageTest8(ageKey='complex',
            name='Котопёсыч',
            animal_type='Котопёёёёёёёёс Котопёос'):
    """Проверяем, что можно добавить питомца
    с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    age = pet_age[ageKey]
    status, result = pf.add_new_pet_without_photo(
            auth_key,
            name,
            animal_type,
            age
    )
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_photo1(photoKey='size_8k',
        name='Киси-Миси',
        animal_type='Хаги-Ваги',
        age='5'
        ):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца
    # и сохраняем в переменную pet_photo
    pet_photo=f'images/{pet_photo_all[photoKey]}'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key,
                    name,
                    animal_type,
                    age,
                    pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_photo2(photoKey='size_10k',
        name='Киси-Миси',
        animal_type='Хаги-Ваги',
        age='5'
        ):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца
    # и сохраняем в переменную pet_photo
    pet_photo=f'images/{pet_photo_all[photoKey]}'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key,
                    name,
                    animal_type,
                    age,
                    pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_photo3(photoKey='bmp',
        name='Киси-Миси',
        animal_type='Хаги-Ваги',
        age='5'
        ):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца
    # и сохраняем в переменную pet_photo
    pet_photo=f'images/{pet_photo_all[photoKey]}'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key,
                    name,
                    animal_type,
                    age,
                    pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_get_all_pets_with_invalid_key(filter=''):
    """ Используя инвалидный ключ, запрашиваем
    список всех питомцев """

    auth_key = invalid_auth_key
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403

    ##################################################
# That's all. Enough. There are 30 negative tests in the one thousand lines. #
    ##################################################