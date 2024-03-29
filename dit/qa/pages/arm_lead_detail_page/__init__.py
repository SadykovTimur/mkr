from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.arm_lead_detail_page.components.problem_card import ProblemCards

__all__ = ['ArmLeadDetailPage']


class ArmLeadDetailPage(Page):
    problem_cards = ProblemCards(css='[class*="tile__problem"]')
    complex_bth = Button(xpath='(//label[@class="ui-radio-buttons-item"])[6]')
    gp_btn = Button(xpath='(//label[@class="ui-radio-buttons-item"])[5]')
    limit_text = Component(xpath="//strong[text()='Нераспределенные лимиты по адресным перечням'] ")
    page_footer = Component(class_name="ui-page-footer")
    page_content = Component(class_name='ui-page-content')
    total_prefecture = Component(xpath="//a[text()='Итого по префектурам']")
    department_housing = Component(xpath="//a[text()='ДЖКХ']")
    department_health = Component(xpath="//a[text()='ДепЗдрав']")
    farming = Component(xpath="//a[text()='Гор.хозяйство (Бирюков П.П.)']")
    transport_name = Component(xpath="//a[text()='Транспорт и дороги (Ликсутов М.С.)']")
    security_name = Component(xpath="//a[text()='Безопасность и инф.политика (Горбенко А.Н.)'] ")
    department_repair = Component(xpath="//div[text()='Департамент капитального ремонта города Москвы']")
    department_transport = Component(xpath="//div[text()='Департамент капитального ремонта города Москвы']")
    department_culture = Component(xpath="//div[text()='Департамент культуры города Москвы']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.limit_text.visible
                assert self.page_footer.visible
                assert self.total_prefecture.visible
                assert self.department_housing.visible

                return self.page_content.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_complex(self):
        complete = self.complex_bth.wait_for_clickability()
        complete.click()

    def wait_for_loading_complex(self) -> None:
        def condition() -> bool:
            try:
                assert self.farming.visible
                assert self.transport_name.visible

                return self.security_name.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_gp_title(self):
        gp_title = self.gp_btn.wait_for_clickability()
        gp_title.click()

    def wait_for_loading_gp_title(self) -> None:
        def condition() -> bool:
            try:
                assert self.department_transport.visible
                assert self.department_repair.visible

                return self.department_culture.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
