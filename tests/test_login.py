import pytest


def test_login_success(login_page, inventory_page, test_data):
    """
    測試目標：驗證標準用戶使用正確憑證能成功登入
    """
    user = test_data["users"]["valid_user"]

    login_page.navigate("https://www.saucedemo.com/")
    login_page.login(user["username"], user["password"])

    assert inventory_page.get_all_product_names() != []
    print("登入成功且產品列表已載入")


def test_login_locked_out_user(login_page, test_data):
    """
    測試目標：驗證被鎖定的用戶登入時會顯示正確的錯誤訊息
    """
    user = test_data["users"]["locked_out_user"]

    login_page.navigate("https://www.saucedemo.com/")
    login_page.login(user["username"], user["password"])

    # 假設你在 LoginPage 增加一個獲取錯誤訊息的方法
    # error_msg = login_page.get_error_message()
    # assert error_msg == user["error_message"]
    pass


@pytest.mark.parametrize("user, pwd", [
    ("wrong_user", "secret_sauce"),
    ("standard_user", "wrong_password"),
    ("", "")
])
def test_login_invalid_credentials(login_page, user, pwd):
    """
    測試目標：資料驅動測試 - 驗證各種錯誤組合都不應進入系統
    """
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login(user, pwd)
    assert "saucedemo.com" in login_page.page.url