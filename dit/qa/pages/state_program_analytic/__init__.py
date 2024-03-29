from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StateProgramAnalyticPage']


class StateProgramAnalyticPage(Page):
    monitoring_control = Button(css='[href="index.php?show=report_edit"]')
    analytic = Component(css='[href="index.php?show=history"]')
    program_text = Component(xpath="//span[text()='Программы и подпрограммы']")
    collection_report = Component(xpath="//div[text()='Сбор отчетности']")
    edit_panel = Component(id="c_editPanel")
    tree_panel = Component(id="c_treePanel")
    state_program_btn = Button(css='[href="index.php?show=actual_gp"]')
    state_program_update = Component(id="phdTitle")
    state_program_actual = Component(id="c_treePanel")
    state_program = Component(id="c_treePanel")
    state_program_actual_text = Component(xpath="//div[contains(text(),'Актуализация государственных программ')]")
    period_btn = Button(id="did_period")
    data_btn = Button(id="lid_period_19809342")
    apply_btn = Button(xpath='(//div[@id="btn_apply"])[1]')
    grid_table = Component(class_name="grid-table-wrap")
    grid_header = Component(class_name="grid-corner-header ")
    params = Component(id="paramsOutput")
    lid_gp_transport = Component(id="lid_gp_23796647")
    lid_gp_events = Component(id="lid_gp_21011897")
    lid_gp_finance = Component(id="lid_gp_21011919")

    def open_report(self) -> None:
        self.monitoring_control.wait_for_clickability()
        self.monitoring_control.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.program_text.visible
                assert self.collection_report.visible
                assert self.edit_panel.visible

                return self.tree_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_state_program(self) -> None:
        self.app.move_to_element(self.analytic.webelement)
        self.state_program_btn.wait_for_clickability()
        self.state_program_btn.click()

    def wait_for_loading_state_program(self) -> None:
        def condition() -> bool:
            try:
                assert self.state_program_update.visible
                assert self.state_program_actual.visible
                assert self.state_program.visible

                return self.state_program_actual_text.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_period(self) -> None:
        self.period_btn.wait_for_clickability()
        self.period_btn.click()
        self.data_btn.wait_for_clickability()
        self.data_btn.click()

    def wait_for_loading_period(self) -> None:
        def condition() -> bool:
            try:
                assert self.params.visible
                assert self.lid_gp_events.visible
                assert self.lid_gp_finance.visible

                return self.lid_gp_transport.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_state_table(self) -> None:
        self.apply_btn.wait_for_clickability()
        self.apply_btn.click()

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
