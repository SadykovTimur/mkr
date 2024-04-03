from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.availability_new_page.components.header import Header
from dit.qa.pages.availability_new_page.components.problem_card import ProblemCards
from dit.qa.pages.availability_new_page.components.problem_details import ProblemDetails

__all__ = ['AvailabilityNewPage']


class AvailabilityNewPage(Page):
    header = Header(class_name='ui-app-header')
    filter = Component(css='[class*="el-options "]')
    problems = ProblemCards(css='[class*="tile__problem"]')
    page_tabs = Component(class_name='ui-page-tabs-header')
    problem_details = ProblemDetails(css="[class*='el-problem-details']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.arm_text == 'ИАС МКР | АРМ РУКОВОДИТЕЛЯ'
                assert self.header.profile == 'АЛЕКСАНДР ЮРЬЕВИЧ ВЕРШИНИН'
                assert self.header.logo.visible

                assert self.filter.visible
                assert self.page_tabs.visible

                return self.problems[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
