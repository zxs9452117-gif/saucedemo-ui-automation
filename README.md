# Web UI Automation Framework (Playwright & Python)

這是一個基於 **Python + Playwright + Pytest** 構建的 UI 自動化測試框架。本專案採用 **Page Object Model (POM)** 設計模式，整合 CI/CD 流程與測試數據管理，旨在展示具備高可維護性、低耦合度且易於擴展的自動化架構。

## 🚀 技術棧
* **語言**: Python 3.10+
* **測試框架**: Pytest
* **自動化工具**: Playwright (優於 Selenium 的自動等待與執行速度)
* **報告工具**: Pytest-HTML / Allure (預留)
* **CI/CD**: GitHub Actions

## 🏗️ 框架架構
本框架採用多層分層設計，確保程式碼的重用性與執行穩定性：
* **BasePage**: 二次封裝 Playwright 核心動作（Click, Fill, Navigate），並統一處理等待邏輯與例外捕獲。
* **PageObjects**: 針對不同頁面（如 Login, Inventory）封裝元素定位與業務行為。
* **Data Driven**: 測試數據獨立存於 `data/test_data.json`，實現測試邏輯與數據解耦。
* **Fixtures**: 利用 `conftest.py` 管理瀏覽器 Context 與 Page Objects 的自動依賴注入。

## 📂 目錄結構
```text
.
├── .github/workflows/      # GitHub Actions CI 配置
├── data/                   # 測試數據層 (JSON)
├── pages/                  # 頁面對象層 (POM)
│   ├── base_page.py        # 基礎方法封裝
│   ├── login_page.py       # 登入頁物件
│   └── inventory_page.py   # 產品頁物件
├── tests/                  # 測試執行層
│   ├── conftest.py         # Pytest Fixtures 與 Hook (失敗截圖)
│   └── test_login.py       # 登入功能測試案例
├── requirements.txt        # 專案依賴清單
└── pytest.ini              # Pytest 全域設定檔
```

## 🔧 環境建置
1. **複製專案**:
   ```bash
   git clone <your-repo-url>
   cd saucedemo-ui-automation
   ```

2. **建立並啟動虛擬環境**:
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate | macOS/Linux: source venv/bin/activate
   ```

3. **安裝依賴與瀏覽器**:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

## 🏃 執行測試
* **執行所有測試**:
    ```bash
    pytest
    ```
* **執行特定標記測試 (如 Smoke Test)**:
    ```bash
    pytest -m smoke
    ```
* **產出 HTML 測試報告**:
    ```bash
    pytest --html=report.html --self-contained-html
    ```

## 🌟 核心亮點
1. **失敗自動截圖 (Failure Screenshots)**: 整合 Pytest Hook，當測試失敗時自動捕捉瀏覽器畫面並存於 `screenshots/`，大幅縮短 Debug 與定位問題的時間。
2. **穩定性優化 (Flakiness Reduction)**: 透過 BasePage 的二次封裝與 Playwright 的 Auto-waiting 機制，有效解決 UI 測試中常見的非同步載入不穩定問題。
3. **CI/CD Pipeline**: 配置 GitHub Actions，確保每次代碼提交 (Push/PR) 皆能自動觸發測試回歸，並將測試結果留存為 Artifacts 供查閱。
4. **標準化配置 (pytest.ini)**: 透過設定檔規範全域執行參數、日誌格式與自定義標記（Markers），建立團隊協作的執行標準。

---
*Authored by Howard*