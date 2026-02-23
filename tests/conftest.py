import pytest
import json
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope="session")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), "../data/test_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n測試失敗，截圖已儲存至: {screenshot_path}")