from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['SubMainMenuWrapper']


class SubMainMenuWrapper(ComponentWrapper):
    submenu = Button(xpath="//b[text()='Агентство по страхованию вкладов']")
    source_sum = Button(xpath="//span[text()='Сумма вкладов '] ")
    toolbar = Text(xpath="//span[text()='Агентство по страхованию вкладов']")
    main_submenu = Component(id="mainSubmenuContent")
    source_blank = Component(id="lind_source_tree_400_1")
    source_deposits = Component(xpath="//span[text()='Возмещение по вкладам и страховая ответственность ']")
    source_insured_deposits = Component(xpath="//span[text()='Средний размер застрахованного вклада ']")


class SubMainMenu(Component):
    def __get__(self, instance, owner) -> SubMainMenuWrapper:
        return SubMainMenuWrapper(instance.app, self.find(instance), self._locator)
