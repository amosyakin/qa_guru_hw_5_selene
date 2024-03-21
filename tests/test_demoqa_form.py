import os.path
from selene import browser, have, command


def test_submit_form():
    browser.open('/')

    browser.element('#userName-wrapper').element('#firstName').type('Ivan')
    browser.element('#userName-wrapper').element('#lastName').type('Ivanov')
    browser.element('#userEmail-wrapper').element('#userEmail').type('ivanivanov@mail.com')
    browser.element('#genterWrapper').element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber-wrapper').element('#userNumber').type('9876543210')
    browser.element('#dateOfBirth-wrapper').click()
    browser.element('.react-datepicker__month-dropdown-container').click().element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2000"]').click()
    browser.element('.react-datepicker__day--001.react-datepicker__day--weekend').click()
    # browser.element('#subjectsWrapper').click().element('#subjectsContainer').type('e')
    browser.element('#hobbiesWrapper').element('#hobbies-checkbox-3').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpg'))
    browser.element('#currentAddress-wrapper').element('#currentAddress').type('Red Square, 1')
    browser.element('#stateCity-wrapper').element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#stateCity-wrapper').element('#city').click().element('#react-select-4-option-2').click()
    browser.element('#submit').click()

    browser.element('.modal-header>div').should(have.text('Thanks for submitting the form'))
    # browser.element('.modal-body').should(have.css_class('table-responsive'))
    browser.element('.modal-footer>button').should(have.text('Close'))
