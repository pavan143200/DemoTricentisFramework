import pytest

from Demo_Tricentis_Framework.pages.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login_page(setup_and_teardown):
    lp= LoginPage(setup_and_teardown)

    lp.click_login()
    lp.enter_email("bubbly123@gmail.com")
    lp.enter_password("Bubbly@123")
    lp.click_login_button()

@pytest.mark.regression
def test_invalid_login_page(setup_and_teardown):
    lp= LoginPage(setup_and_teardown)

    lp.click_login()
    lp.enter_email("bub123@gmail.com")
    lp.enter_password("Bly@123")
    lp.click_login_button()

#Read Excel data
'''
from Demo_Tricentis_Framework.utilities import read_excel
@pytest.mark.smoke
@pytest.mark.parametrize("username,password",read_excel.get_data())
def test_valid_login_page(setup_and_teardown,username,password  ):
    lp= LoginPage(setup_and_teardown)

    lp.click_login()
    lp.enter_email(username)
    lp.enter_password(password)
    lp.click_login_button()
'''
