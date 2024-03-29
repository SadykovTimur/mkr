from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ReportsEhdPage']


class ReportsEhdPage(Page):
    submenu = Button(xpath="//b[text()='Агентство по страхованию вкладов']")
    toolbar = Component(class_name="subToolbar")
    main_submenu = Component(id="mainSubmenuContent")
    source_blank = Component(id="lind_source_tree_400_1")
    source_deposits = Component(id="lind_source_tree_400_2")
    source_insured_deposits = Component(id="lind_source_tree_400_7")
    source_sum = Button(id="lind_source_tree_400_13")
    content_table = Component(id="contentAll_1")
    content_body = Component(class_name="grid-body-content")
    toolbar_toptool = Component(id="toolbar_inds")
    toolbar_param = Component(id="dopParam")

    def open_menu(self):
        self.submenu.wait_for_clickability()
        self.submenu.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.toolbar.visible
                assert self.main_submenu.visible
                assert self.source_blank.visible
                assert self.source_deposits.visible

                return self.source_insured_deposits.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_report(self):
        self.source_sum.wait_for_clickability()
        self.source_sum.click()

    def wait_for_loading_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.content_table.visible
                assert self.content_body.visible
                assert self.toolbar_toptool.visible

                return self.toolbar_param.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
