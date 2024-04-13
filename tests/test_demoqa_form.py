import os.path
from selene import browser, have, command, by
from qa_guru_5_hw_selene.data.users import User
from qa_guru_5_hw_selene.model.pages.registration_page import RegistrationPage


def test_submit_form():
    user = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivanivanov@mail.com',
        gender='Male',
        phone_number='9876543210',
        birth_day='01',
        birth_month='January',
        birth_year='2000',
        subjects='English',
        hobbies='Music',
        picture_path='picture.jpg',
        address='Red Square, 1',
        state='Haryana',
        city='Karnal'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)
