from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.state_program_report_page.components.header import Header
from dit.qa.pages.state_program_report_page.components.tree_panel import TreePanel

__all__ = ['StateProgramReportPage']


class StateProgramReportPage(Page):
    header = Header(id="h-content")
    breadcrumbs = Text(id="breadcrumbs-menu")
    tree_panel = TreePanel(id="c_treePanel")
    edit_panel = Component(id="c_editPanel")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.items_news.visible
                assert self.header.items_data.visible
                assert self.header.items_analytica.visible
                assert self.header.items_service.visible
                assert self.header.title == 'ИАС МКР'
                assert self.header.logo.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'

                assert "Сбор отчетности" in self.breadcrumbs
                assert "Госпрограммы" in self.breadcrumbs
                assert self.tree_panel.state_program.visible

                return self.edit_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
