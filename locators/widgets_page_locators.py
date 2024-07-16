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
    MULTI_VALUE_REMOVE = (
    'xpath', '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]//*[local-name() = "path"]')
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


class SliderPageLocators:
    INPUT_SLIDER = ('xpath', '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = ('xpath', '//input[@id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = ('xpath', '//button[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = ('xpath', '//div[@class="progress-bar bg-info"]')


class TabsPageLocators:
    TABS_WHAT = ('xpath', '//a[@id="demo-tab-what"]')
    TABS_WHAT_CONTENT = ('xpath', '//div[@id="demo-tabpane-what"]')
    TABS_ORIGIN = ('xpath', '//a[@id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = ('xpath', '//div[@id="demo-tabpane-origin"]')
    TABS_USE = ('xpath', '//a[@id="demo-tab-use"]')
    TABS_USE_CONTENT = ('xpath', '//div[@id="demo-tabpane-use"]')
    TABS_MORE = ('xpath', '//a[@id="demo-tab-more"]')
    TABS_MORE_CONTENT = ('xpath', '//div[@id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = ('xpath', '//button[@id="toolTipButton"]')
    TOOL_TIP_BUTTON = ('xpath', '//button[@aria-describedby="buttonToolTip"]')

    FIELD = ('xpath', '//input[@id="toolTipTextField"]')
    TOOL_TIP_FIELD = ('xpath', '//input[@aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = ('xpath', '//a[text()="Contrary"]')
    TOOL_TIP_CONTRARY= ('xpath', '//a[@aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = ('xpath', '//a[text()="1.10.32"]')
    TOOL_TIP_SECTION = ('xpath', '//a[@aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = ('xpath', '//div[@class="tooltip-inner"]')
