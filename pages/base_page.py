
class BasePage():
    
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    #открывает нужную страницу в браузере
    def open(self): 
        self.browser.get(self.url)