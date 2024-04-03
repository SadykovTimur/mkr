from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(css='[alt="logo"]')
    title = Text(tag='h1')
    user_info = Text(css='[class*="user-info"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.title == 'МКР'
        assert 'FTest' in self.user_info

        return 'Вершинин А. Ю.' in self.user_info


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
