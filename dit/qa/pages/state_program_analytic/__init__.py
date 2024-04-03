from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.state_program_analytic.components.header import Header
from dit.qa.pages.state_program_analytic.components.main import Main
from dit.qa.pages.state_program_analytic.components.settings_panel import SettingsPanel

__all__ = ['StateProgramAnalyticPage']


class StateProgramAnalyticPage(Page):
    header = Header(id="h-content")
    settings_panel = SettingsPanel(id="c_settingsPanel")
    breadcrumbs = Text(id="breadcrumbs-menu")
    monitoring_control = Button(xpath="//a[text()='Сбор отчетности']")
    main = Main(id="main-content")
    state_program_btn = Button(xpath='//a[text()="	Актуализация государственных программ"]')
    data_btn = Button(id="lid_period_19809342")
    grid_table = Component(class_name="grid-table-wrap")
    grid_header = Component(class_name="grid-corner-header ")
    gp_name_1 = Component(xpath="//span[text()='01.05.003.003']")
    gp_name_2 = Component(xpath="//span[text()='01.05.005.006']")

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
                assert "Программы и подпрограммы" in self.main.program_text
                assert self.main.editPanel.visible

                return self.main.treePanel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_state_program(self) -> None:
        self.app.move_to_element(self.header.items_analytica.webelement)
        self.state_program_btn.click()

    def wait_for_loading_state_program(self) -> None:
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

                assert "Аналитика" in self.breadcrumbs
                assert self.main.repPanel.visible
                assert "Актуализация государственных программ" in self.breadcrumbs
                assert "Государственные программы" in self.main.state_program

                return "Актуализация государственных программ" in self.main.state_program_update

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_state_program_table(self) -> None:
        def condition() -> bool:
            try:
                assert self.gp_name_1.visible

                return self.gp_name_2.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_state_table(self) -> None:
        def condition() -> bool:
            try:
                assert self.grid_table.visible

                return self.grid_header.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
