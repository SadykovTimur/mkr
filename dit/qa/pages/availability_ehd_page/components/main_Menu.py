from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['MainMenuWrapper']


class MainMenuWrapper(ComponentWrapper):
    news = Component(id="menu_news")
    manage = Component(id="menu_manage")
    office = Component(id="menu_office")
    reps_info = Component(css='[onmouseover="getHtmlRepsInfo()"]')
    docs_info = Component(css='[onmouseover="getHtmlDocsInfo()"]')
    gor = Component(id="menu_gor")


class MainMenu(Component):
    def __get__(self, instance, owner) -> MainMenuWrapper:
        return MainMenuWrapper(instance.app, self.find(instance), self._locator)
