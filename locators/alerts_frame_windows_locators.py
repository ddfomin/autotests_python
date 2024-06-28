class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = ("xpath", "//button[@id='tabButton']")
    TITLE_NEW = ("xpath", "//h1[@id='sampleHeading']")
    NEW_WINDOW_BUTTON = ("xpath", "//button[@id='windowButton']")

class AlertsPageLocators:
    SEE_ALERT_BUTTON = ("xpath", "//button[@id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = ("xpath", "//button[@id='confirmButton']")
    CONFIRM_RESULT = ("xpath", "//span[@id='confirmResult']")
    PROMPT_BOX_ALERT_BUTTON = ("xpath", "//button[@id='promtButton']")
    PROMPT_RESULT = ("xpath", "//span[@id='promptResult']")
