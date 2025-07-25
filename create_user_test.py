import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

def negative_assert(first_name):
     user_body = get_user_body("first_name")
     user_response = sender_stand_request.post_new_user(user_body)
     assert user_response.status_code == 400



def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def test_create_user_letter_in_first_name_get_success_response():
    negative_assert("A")

def test_create_user_16_letter_in_last_name_get_success_response():
    negative_assert("Aaaaaaaaaaaaaaaa")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert("A Aaa")

def test_create_user_special_characters_in_first_name_get_error_response():
    negative_assert("№%@")

def test_create_user_numbers_in_fist_name_get_error_response():
    negative_assert("123")

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")  # eliminar el parámetro
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400


def test_create_user_empty_first_name_get_error_response():
    negative_assert("")


def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400


