from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(css='[class*="logo__img"]')
    arm_text = Text(css='[class*="logo__title"]')
    profile = Text(css='[class*="profile__name"]')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
