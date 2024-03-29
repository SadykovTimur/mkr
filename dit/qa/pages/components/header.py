from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    login = Button(class_name='login-button ')
    logo = Component(class_name='the-header ')
    profile_name = Component(xpath="//span[text()='Вершинин А. Ю.']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
