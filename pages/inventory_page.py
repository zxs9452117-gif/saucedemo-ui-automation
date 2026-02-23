from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._inventory_container = ".inventory_list"
        self._item_names = ".inventory_item_name"
        self._add_to_cart_btns = "button[data-test^='add-to-cart']"
        self._shopping_cart_badge = ".shopping_cart_badge"
        self._product_sort_container = "[data-test='product_sort_container']"

    def get_all_product_names(self):
        """獲取所有產品名稱列表"""
        return self.page.locator(self._item_names).all_text_contents()

    def add_first_item_to_cart(self):
        """將列表中的第一個商品加入購物車"""
        self.do_click(f"({self._add_to_cart_btns}) >> nth=0")

    def add_item_by_name(self, name):
        """根據產品名稱點擊加入購物車 (動態定位)"""
        selector = f".inventory_item:has-text('{name}') >> button"
        self.do_click(selector)

    def get_cart_count(self):
        """獲取購物車顯示的數字"""
        if self.page.locator(self._shopping_cart_badge).is_visible():
            return self.page.locator(self._shopping_cart_badge).inner_text()
        return "0"

    def sort_products(self, option_value):
        """選擇排序方式"""
        self.page.select_option(self._product_sort_container, option_value)