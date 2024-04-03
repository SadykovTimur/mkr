from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['ContainerWrapper']


class ContainerWrapper(ComponentWrapper):
    content_body = Component(class_name="grid-body-content")
    toolbar_toptool = Text(id="toolbar_inds")
    filter = Text(id="div_fltr_cont")


class Container(Component):
    def __get__(self, instance, owner) -> ContainerWrapper:
        return ContainerWrapper(instance.app, self.find(instance), self._locator)
