from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.availability_ehd_page.components.main_Container import MainContainer
from dit.qa.pages.availability_ehd_page.components.main_Menu import MainMenu

__all__ = ['AvailabilityEhdPage']


class AvailabilityEhdPage(Page):
    main_menu = MainMenu(class_name='mainMenu')
    main_Container = MainContainer(class_name='mainContainer')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.main_menu.news.visible
                assert self.main_menu.manage.visible
                assert self.main_menu.office.visible
                assert self.main_menu.reps_info.visible
                assert self.main_menu.docs_info.visible
                assert self.main_menu.gor.visible
                assert self.main_Container.search.visible
                assert self.main_Container.globe.visible
                assert self.main_Container.help.visible
                assert self.main_Container.feedback.visible
                assert self.main_Container.user.visible
                assert self.main_Container.all_news.visible
                assert self.main_Container.all_news_rss.visible

                return self.main_Container.container.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
