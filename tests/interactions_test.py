from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'the order of the list has not been changed'
            assert grid_before != grid_after, 'the order of the list has not been changed'

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_element_list = selectable_page.select_list_item()
            active_element_grid = selectable_page.select_grid_item()
            assert len(active_element_list) > 0, 'no element were selected'
            assert len(active_element_grid) > 0, 'no element were selected'

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, mix_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, 'maximum size not equal to "500px", "300px"'
            assert ('150px', '150px') == min_box, 'maximum size not equal to "150px", "150px"'
            assert mix_resize != max_resize, 'resizable has not been changed'

    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', "the elements has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_acceptable, acceptable = droppable_page.drop_accept()
            assert not_acceptable == 'Drop here', "the dropped element has been accepted"
            assert acceptable == 'Dropped!', "the dropped element has not been accepted"

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', "the elements texts has not been changed"
            assert not_greedy_inner == 'Dropped!', "the elements texts has not been changed"
            assert greedy == 'Outer droppable', "the elements texts has been changed"
            assert greedy_inner == 'Dropped!', "the elements texts has not been changed"

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revent = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revent = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revent, 'the elements has not reverted'
            assert not_will_after_move == not_will_after_move, 'the elements has reverted'

    class TestDraggablePage:
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_dra_box()
            assert before != after, 'the position of the box has not been changed'

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted('x')
            top_y, left_y = draggable_page.axis_restricted('y')
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, ('box position has not changed or there has '
                                                                          'been a shift in the y-axis')
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, ('box position has not changed or there '
                                                                             'has been a shift in the y-axis')
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, ('box position has not changed or there has '
                                                                          'been a shift in the x-axis')
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, ('box position has not changed or there '
                                                                             'has been a shift in the x-axis')
