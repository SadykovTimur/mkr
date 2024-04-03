from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['ReportPanel']


class ReportPanelWrapper(ComponentWrapper):
    state_program_update = Component(xpath="//span[text()='Актуализация государственных программ']")
    grid_table = Component(class_name="grid-table-wrap")


class ReportPanel(Component):
    def __get__(self, instance, owner) -> ReportPanelWrapper:
        return ReportPanelWrapper(instance.app, self.find(instance), self._locator)
