import pytest
from selene.support.shared import browser
from selene import be, have


browser.open('https://yahoo.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))
