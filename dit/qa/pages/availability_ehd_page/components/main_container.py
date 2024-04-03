from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['MainContainer']


class MainContainerWrapper(ComponentWrapper):
    search = Component(id="srch")
    globe = Component(css='[class*="menu-mapconstructor"]')
    help = Component(css='[class*="menu-help"]')
    feedback = Component(css='[class*="menu-feedback"]')
    user = Component(css='[class*="menu-user"]')
    all_news = Component(id="all_news")
    all_news_rss = Component(id="all_news_rss")
    container = Component(id="content-container")
    content_body = Component(class_name="grid-body-content")
    toolbar_toptool = Text(id="toolbar_inds")
    filter = Text(id="div_fltr_cont")


class MainContainer(Component):
    def __get__(self, instance, owner) -> MainContainerWrapper:
        return MainContainerWrapper(instance.app, self.find(instance), self._locator)
