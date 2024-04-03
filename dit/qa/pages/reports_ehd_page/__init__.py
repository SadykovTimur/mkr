from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.reports_ehd_page.components.container import Container
from dit.qa.pages.reports_ehd_page.components.sub_main_menu import SubMainMenu

__all__ = ['ReportsEhdPage']


class ReportsEhdPage(Page):
    menu = SubMainMenu(class_name="mainSubmenu")
    container = Container(class_name="mainContainer")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert "Агентство по страхованию вкладов" in self.menu.toolbar
                assert self.menu.main_submenu.visible
                assert self.menu.source_blank.visible
                assert self.menu.source_deposits.visible

                return self.menu.source_insured_deposits.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.container.content_body.visible
                assert "Вид представления: На первую дату периода; Территория: г. Москва" in self.container.filter

                return "Сумма вкладов, млн руб." in self.container.toolbar_toptool

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
