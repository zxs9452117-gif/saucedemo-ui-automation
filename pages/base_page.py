class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click_element(self, selector):
        self.page.click(selector)

    def fill_input(self, selector, text):
        self.page.fill(selector, text)