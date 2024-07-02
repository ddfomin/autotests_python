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

class FramesPageLocators:
    FIRST_FRAME = ("xpath", "//iframe[@id='frame1']")
    SECOND_FRAME = ("xpath", "//iframe[@id='frame2']")
    TITLE_FRAME = ("xpath", "//h1[@id='sampleHeading']")

class NestedFramePageLocators:
    PARENT_FRAME = ("xpath", "//iframe[@id='frame1']")
    PARENT_TEXT = ("xpath", "//body")
    CHILD_FRAME = ("xpath", "//iframe[@srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = ("xpath", "//p")

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = ("xpath", "//button[@id='showSmallModal']")
    SMALL_MODAL_CLOSE_BUTTON = ("xpath", "//button[@id='closeSmallModal']")
    BODY_SMALL = ("xpath", "//div[@class='modal-body']")
    TITLE_SMALL_MODAL = ("xpath", "//div[@id='example-modal-sizes-title-sm']")
    LARGE_MODAL_BUTTON = ("xpath", "//button[@id='showLargeModal']")
    BODY_LARGE = ("xpath", "//div[@class='modal-body']//p")
    TITLE_LARGE_MODAL = ("xpath", "//div[@id='example-modal-sizes-title-lg']")
