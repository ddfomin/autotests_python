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
