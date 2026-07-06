import pytest
from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()


#Cross browser testing:

'''@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):
    parameter= request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'edge':
        driver = webdriver.Edge()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()'''