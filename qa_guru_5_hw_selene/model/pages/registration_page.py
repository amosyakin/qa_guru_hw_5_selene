from selene import browser, by, command, have

from qa_guru_5_hw_selene import resources
from qa_guru_5_hw_selene.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.subjects_input = browser.element('#subjectsInput')
        self.up_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')
        self.close_large_modal = browser.element('#closeLargeModal')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.email)
        browser.element(by.text(user.gender)).perform(command.js.click)
        self.user_number.type(user.phone_number)
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view)
        browser.element('#dateOfBirthInput').perform(command.js.click)
        browser.element('.react-datepicker__month-select').click().element(by.text(user.birth_month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(user.birth_year)).click()
        browser.element(
            f'.react-datepicker__day--0{user.birth_day}:not(.react-datepicker__day--outside-month)'
        ).click()
        self.subjects_input.type(user.short_subject())
        browser.element(by.text(user.subjects)).perform(command.js.click)
        browser.element(by.text(user.hobbies)).perform(command.js.click)
        self.up_picture.set_value(resources.path(user.picture_path))
        self.current_address.type(user.address)
        self.state.click()
        browser.element(by.text(user.state)).perform(command.js.click)
        self.city.click()
        browser.element(by.text(user.city)).perform(command.js.click)
        self.submit.click()

    def should_have_registered(
            self, user: User):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.full_name(),
                user.email,
                user.gender,
                user.phone_number,
                user.date_of_birth(),
                user.subjects,
                user.hobbies,
                user.picture_path,
                user.address,
                user.state_and_city()))
        self.close_large_modal.should(have.text('Close'))
