import time
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page = ProductPage(browser, url)
    main_page.open()                      # открываем страницу
    time.sleep(2)
    product_page.add_product()
    time.sleep(2)
    main_page.solve_quiz_and_get_code()
    time.sleep(2)
    product_page.check_add_notify("The shellcoder's handbook has been added to your basket.")
    product_page.check_basket_total("Your basket total is now £9.99")