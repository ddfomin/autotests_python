class SortablePageLocators:
    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    LIST_ITEM = ('xpath', '//div[@id="demo-tabpane-list"] //div[@class="list-group-item list-group-item-action"]')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    GRID_ITEM = ('xpath', '//div[@id="demo-tabpane-grid"] //div[@class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    LIST_ITEM = ('xpath', '//li[@class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = ('xpath', '//li[@class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    GRID_ITEM = ('xpath', '//li[@class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = ('xpath', '//li[@class="list-group-item active list-group-item-action"]')

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = ('xpath', '(//span[@class="react-resizable-handle react-resizable-handle-se"])[1]')
    RESIZABLE_BOX = ('xpath', '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = ('xpath', '(//span[@class="react-resizable-handle react-resizable-handle-se"])[2]')
    RESIZABLE = ('xpath', '//div[@id="resizable"]')
