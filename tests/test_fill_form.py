import os

from selene import browser, have, be


def test_fill_form():
    browser.open(browser.config.base_url)
    browser.should(have.title_containing('DEMOQA'))

    browser.element('[id="firstName"]').clear().type('John')

    browser.element('[id="lastName"]').clear().type('Doe')

    browser.element('[id="userEmail"]').clear().type('gte@mail.com')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('[id="userNumber"]').clear().type('1234567890')

    browser.element('[id="dateOfBirthInput"]').click()
    (browser.element('.react-datepicker__month-select').should(be.visible)
     .element('option[value="7"]').click())
    (browser.element('.react-datepicker__year-select').should(be.visible)
     .element('option[value="2023"]').click())
    (browser.element('.react-datepicker__day').should(be.visible)
     .element('//*[text()="7"]').click())

    (browser.element('[id="subjectsInput"]').clear().type('Eng'))
    browser.element('.subjects-auto-complete__option').element('//*[text()="English"]').click()

    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('../pic.jpeg'))

    browser.element('[id="currentAddress"]').clear().type('123 Main St')

    (browser.element('[id="state"]').click()
     .element('[id="react-select-3-option-2"]').click())

    (browser.element('[id="city"]').click()
     .element('[id="react-select-4-option-0"]').click())

    browser.element('[id="submit"]').click()
    browser.element('[class="table-responsive"]').should(be.visible)

    browser.element("//td[contains(text(), 'Student Name')]/following-sibling::td").should(have.text('John Doe'))
    browser.element("//td[contains(text(), 'Student Email')]/following-sibling::td").should(have.text('gte@mail.com'))
    browser.element("//td[contains(text(), 'Gender')]/following-sibling::td").should(have.text('Male'))
    browser.element("//td[contains(text(), 'Mobile')]/following-sibling::td").should(have.text('1234567890'))
    browser.element("//td[contains(text(), 'Date of Birth')]/following-sibling::td").should(have.text('07 August,2023'))
    browser.element("//td[contains(text(), 'Subjects')]/following-sibling::td").should(have.text('English'))
    browser.element("//td[contains(text(), 'Hobbies')]/following-sibling::td").should(have.text('Sports'))
    browser.element("//td[contains(text(), 'Picture')]/following-sibling::td").should(have.text('pic.jpeg'))
    browser.element("//td[contains(text(), 'Address')]/following-sibling::td").should(have.text('123 Main St'))
    browser.element("//td[contains(text(), 'State and City')]/following-sibling::td").should(have.text('Haryana Karnal'))
