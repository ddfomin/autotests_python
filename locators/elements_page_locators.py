class TextBoxPageLocators:
    # form field
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    # created form
    CREATED_FULL_NAME = ("xpath", "//p[@id='name']")
    CREATED_EMAIL = ("xpath", "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    CHECKED_ITEMS = ("css selector", "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = ("xpath", "//label[@class='custom-control-label' and @for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = ("xpath", "//label[@class='custom-control-label' and @for='impressiveRadio']")
    NO_RADIOBUTTON = ("xpath", "//label[@class='custom-control-label disabled' and @for='noRadio']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = ("xpath", "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = ("xpath", "//input[@id='firstName']")
    LASTNAME_INPUT = ("xpath", "//input[@id='lastName']")
    EMAIL_INPUT = ("xpath", "//input[@id='userEmail']")
    AGE_INPUT = ("xpath", "//input[@id='age']")
    SALARY_INPUT = ("xpath", "//input[@id='salary']")
    DEPARTMENT_INPUT = ("xpath", "//input[@id='department']")
    SUBMIT = ("xpath", "//button[@id='submit']")

    # table
    FULL_PEOPLE_LIST = ("xpath", "//div[@class='rt-tr-group']")
    SEARCH_INPUT = ("xpath", "//input[@id='searchBox']")
    DELETE_BUTTON = ("xpath", "//span[@title='Delete']")
    ROW_PARENT = (".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = ("xpath", "//div[@class='rt-noData']")
    COUNT_ROW_LIST = ("xpath", "//select[@aria-label='rows per page']")

    # update
    UPDATE_BUTTON = ("xpath", "//span[@title='Edit']")


class ButtonsPageLocators:
    DOUBLE_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")

    # result
    DOUBLE_BUTTON_MESSAGE = ("xpath", "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_BUTTON_MESSAGE = ("xpath", "//p[@id='rightClickMessage']")
    CLICK_ME_BUTTON_MESSAGE = ("xpath", "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    SIMPLE_LINK = ("xpath", "//a[@id='simpleLink']")
    BAD_REQUEST = ("xpath", "//a[@id='bad-request']")


class UploadAndDownloadLocators:
    UPLOAD_FILE = ("xpath", "//input[@type='file']")
    UPLOADED_RESULT = ("xpath", "//p[@id='uploadedFilePath']")

    DOWNLOAD_FILE = ("xpath", "//a[@id='downloadButton']")


class DynamicPropertiesPageLocators:
    ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
    COLOR_CHANGE_BUTTON = ("xpath", "//button[@id='colorChange']")
    VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
