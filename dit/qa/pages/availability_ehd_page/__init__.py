from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.availability_ehd_page.components.main_container import MainContainer
from dit.qa.pages.availability_ehd_page.components.main_menu import MainMenu
from dit.qa.pages.availability_ehd_page.components.sub_main_menu import SubMainMenu

__all__ = ['AvailabilityEhdPage']


class AvailabilityEhdPage(Page):
    main_menu = MainMenu(class_name='mainMenu')
    main_container = MainContainer(class_name='mainContainer')
    menu = SubMainMenu(class_name="mainSubmenu")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.main_menu.news.visible
                assert self.main_menu.manage.visible
                assert self.main_menu.office.visible
                assert self.main_menu.reps_info.visible
                assert self.main_menu.docs_info.visible
                assert self.main_menu.gor.visible

                assert self.main_container.search.visible
                assert self.main_container.globe.visible
                assert self.main_container.help.visible
                assert self.main_container.feedback.visible
                assert self.main_container.user.visible
                assert self.main_container.all_news.visible
                assert self.main_container.all_news_rss.visible

                return self.main_container.container.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_submenu(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.toolbar.visible
                assert self.menu.source_blank.visible
                assert self.menu.source_deposits.visible

                return self.menu.source_insured_deposits.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Submenu was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.main_container.content_body.visible
                assert self.main_container.filter == "Вид представления: На первую дату периода; Территория: г. Москва"

                return "Сумма вкладов, млн руб." in self.main_container.toolbar_toptool

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Report was not loaded')
        self.app.restore_implicitly_wait()
