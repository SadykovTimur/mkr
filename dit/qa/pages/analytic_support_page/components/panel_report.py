from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['PanelReport']


class PanelReportWrapper(ComponentWrapper):
    body_content = Component(class_name="grid-body-content")
    title = Component(css='[title="Отчет по мерам социальной поддержки "]')


class PanelReport(Component):
    def __get__(self, instance, owner) -> PanelReportWrapper:
        return PanelReportWrapper(instance.app, self.find(instance), self._locator)
