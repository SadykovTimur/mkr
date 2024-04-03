from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['MainContainerWrapper']


class MainContainerWrapper(ComponentWrapper):
    search = Component(id="srch")
    globe = Component(css='[metatitle="Конструктор карт"]')
    help = Component(css='[metatitle="Помощь"]')
    feedback = Component(css='[metatitle="Обратная связь"]')
    user = Component(css='[metatitle="Пользователь"]')
    all_news = Component(id="all_news")
    all_news_rss = Component(id="all_news_rss")
    container = Component(id="content-container")


class MainContainer(Component):
    def __get__(self, instance, owner) -> MainContainerWrapper:
        return MainContainerWrapper(instance.app, self.find(instance), self._locator)
