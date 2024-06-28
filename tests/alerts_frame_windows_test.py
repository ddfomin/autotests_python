from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened("tab")
            assert text_result == "This is a sample page", "the new tab has not opened or an incorrect tab has opened"


