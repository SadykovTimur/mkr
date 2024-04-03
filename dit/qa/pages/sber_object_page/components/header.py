from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Component(xpath="//strong[contains(text(),'ИАС МКР')]")
    arm_data = Component(xpath='//a[text()="Формирование данных"]')
    arm_object = Button(xpath='//a[text()="Объекты"]')
    arm_data_lot = Component(xpath='//a[text()="Передача потребностей в ЕАИСТ"] ')
    name = Component(xpath="//span[text()='Вершинин А. Ю.']")
    login = Component(xpath="//span[text()='FTest']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
