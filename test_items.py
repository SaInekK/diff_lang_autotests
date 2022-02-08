def test_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements_by_css_selector("input[type=submit]")
    assert button != [], 'No basket button element found'
