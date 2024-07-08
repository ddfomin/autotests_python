class AccordianPageLocators:
    SECTION_FIRST = ('xpath', '//div[@id="section1Heading"]')
    SECTION_CONTENT_FIRST = ('xpath', '//div[@id="section1Content"]//p')
    SECTION_SECOND = ('xpath', '//div[@id="section2Heading"]')
    SECTION_CONTENT_SECOND = ('xpath', '//div[@id="section2Content"]//p')
    SECTION_THIRD = ('xpath', '//div[@id="section3Heading"]')
    SECTION_CONTENT_THIRD = ('xpath', '//div[@id="section3Content"]//p')

class AutoCompletePageLocators:
    MULTI_INPUT = ('xpath', '//input[@id="autoCompleteMultipleInput"]')
    MULTI_VALUE = ('xpath', '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = ('xpath', '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]//*[local-name() = "path"]')
    SINGLE_VALUE = ('xpath', '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = ('xpath', '//input[@id="autoCompleteSingleInput"]')

class DataPickerPageLocators:
    # date
    DATE_INPUT = ('xpath', '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = ('xpath', '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEARS = ('xpath', '//select[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = ('xpath', '//div[contains(@class, "react-datepicker__day react-datepicker__day")]')
    # date and time
    DATE_AND_TIME_INPUT = ('xpath', '//input[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = ('xpath', '//div[@class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEARS = ('xpath', '//div[@class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = ('xpath', '//li[@class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = ('xpath', '//div[contains(@class, "react-datepicker__month-option")]')
    DATE_AND_TIME_YEAR_LIST = ('xpath', '//div[contains(@class, "react-datepicker__year-option")]')