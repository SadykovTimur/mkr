from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['SberObjectPage']


class SberObjectPage(Page):
    object = Button(
        xpath="//div[@class='ui-popover header-menu-list']//a[@class='header-menu-list__link' and text()='Объекты']"
    )
    apply_btn = Button(xpath='(//button[@type="button"])[50] ')
    object_list = Component(xpath="//span[text()='Список объектов']")
    filter_options = Component(xpath="//span[text()='Параметры и фильтры']")
    tab = Component(css='[class="ui-tab"]')
    id_object = Component(xpath="//span[text()='ID объекта']")
    category_object = Component(xpath="//span[text()='Категория объекта']")
    address_object = Component(xpath="//span[text()='Адрес/местоположение']")
    archive_object = Component(xpath="//span[text()='Архив']")
    educational_organization = Component(xpath="//span[text()='профессиональная образовательная организация']")
    address_fighting = Component(xpath="//span[text()='Бойцовая улица д.6 к.8Б']")
    object_road_net = Component(xpath="//span[text()='Объекты улично-дорожной сети']")
    address_travel = Component(xpath="//span[text()='Проезд вблизи д. Ямонтово']")

    def open_object(self) -> None:
        self.object.wait_for_clickability()
        self.object.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.object_list.visible

                return self.filter_options.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_apply(self) -> None:
        self.apply_btn.wait_for_clickability()
        self.apply_btn.click()

    def wait_for_loading_object(self) -> None:
        def condition() -> bool:
            try:
                assert self.id_object.visible
                assert self.category_object.visible
                assert self.address_object.visible
                assert self.archive_object.visible
                assert self.educational_organization.visible
                assert self.object_road_net.visible
                assert self.address_fighting.visible

                return self.address_travel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
