from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.state_program_analytic_page.components.header import Header
from dit.qa.pages.state_program_analytic_page.components.report_panel import ReportPanel
from dit.qa.pages.state_program_analytic_page.components.settings_panel import SettingsPanel
from dit.qa.pages.state_program_analytic_page.components.tree_panel import TreePanel

__all__ = ['StateProgramAnalyticPage']


class StateProgramAnalyticPage(Page):
    header = Header(id="h-content")
    breadcrumbs = Text(id="breadcrumbs-menu")
    data_btn = Button(xpath='//li[text()="2019"]')
    settings_panel = SettingsPanel(id="c_settingsPanel")
    treePanel = TreePanel(id="c_treePanel")
    repPanel = ReportPanel(id="c_repPanel")

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

                assert "Госпрограммы" in self.breadcrumbs
                assert "Аналитика" in self.breadcrumbs
                assert "Актуализация государственных программ" in self.breadcrumbs
                assert self.settings_panel.visible
                assert self.treePanel.state_program.visible

                return self.repPanel.state_program_update.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_state_program_table(self) -> None:
        def condition() -> bool:
            try:
                return self.treePanel.items[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Program was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_state_table(self) -> None:
        def condition() -> bool:
            try:
                return self.repPanel.grid_table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Table was not loaded')
        self.app.restore_implicitly_wait()
