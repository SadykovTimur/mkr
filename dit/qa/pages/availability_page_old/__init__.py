from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AvailabilityOldPage']


class AvailabilityOldPage(Page):
    closeBtn = Button(class_name='ui-win-clsBtn ')
    book_name = Component(id='bookName')
    book_secname = Component(id='bookSecName')
    problem_group = Component(id="problem_group_con")
    simple_tabset = Component(class_name='simple-tabset')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.book_name.visible
                assert self.book_secname.visible
                assert self.problem_group.visible

                return self.simple_tabset.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()