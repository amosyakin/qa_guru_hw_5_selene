import os.path
from selene import browser, have, command, by


def test_submit_form():
    browser.open('/')

    browser.element('#userName-wrapper').element('#firstName').type('Ivan')
    browser.element('#userName-wrapper').element('#lastName').type('Ivanov')
    browser.element('#userEmail-wrapper').element('#userEmail').type('ivanivanov@mail.com')
    browser.element('#genterWrapper').element(by.text('Male')).perform(command.js.click)
    browser.element('#userNumber-wrapper').element('#userNumber').type('9876543210')
    browser.element('#dateOfBirth-wrapper').element('#dateOfBirthInput').perform(command.js.click)
    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2000')).click()
    browser.element('.react-datepicker__week').element(by.text('1')).click()
    browser.element('#subjectsWrapper').element('#subjectsInput').type('en')
    browser.element(by.text('English')).click()
    browser.element('#hobbiesWrapper').element(by.text('Music')).perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpg'))
    browser.element('#currentAddress-wrapper').element('#currentAddress').type('Red Square, 1')
    browser.element('#stateCity-wrapper').perform(command.js.scroll_into_view)
    browser.element('#stateCity-wrapper').element('#state').click().element(by.text('Haryana')).click()
    browser.element('#stateCity-wrapper').element('#city').click().element(by.text('Karnal')).click()
    browser.element('#submit').click()

    browser.element('.modal-header>div').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Ivan Ivanov', 'ivanivanov@mail.com', 'Male', '9876543210', '01 January,2000',
        'English', 'Music', 'picture.jpg', 'Red Square, 1', 'Haryana Karnal'))
    browser.element('.modal-footer>button').should(have.text('Close'))
