import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened(self, check):
        if check == "tab":
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title_tab = self.element_is_present(self.locators.TITLE_NEW).text
            return text_title_tab
        elif check == "window":
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title_window = self.element_is_present(self.locators.TITLE_NEW).text
            return text_title_window
