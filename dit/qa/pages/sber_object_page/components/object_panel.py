from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['ObjectPanel']


class ObjectPanelWrapper(ComponentWrapper):
    object_list = Component(xpath="//span[text()='Список объектов']")
    id_object = Component(xpath="//span[text()='ID объекта']")
    category_object = Component(xpath="//span[text()='Категория объекта']")
    address_object = Component(xpath="//span[text()='Адрес/местоположение']")
    archive_object = Component(xpath="//span[text()='Архив']")


class ObjectPanel(Component):
    def __get__(self, instance, owner) -> ObjectPanelWrapper:
        return ObjectPanelWrapper(instance.app, self.find(instance), self._locator)
