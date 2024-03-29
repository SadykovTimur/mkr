from typing import Callable
import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import open_auth_form, open_start_page, open_start_page_after_auth, sign_in, open_availability_hand_new, open_arm_lead_detail


@allure.label('owner', 't.sadykov')
@allure.label('component', 'MKR')
@allure.epic('MKR')
@allure.story('Вход в подсистему "АРМ Руководителя новый"')
@allure.title('Проверка детализации показателей проблемы')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_arm_lead_detail(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)
    open_auth_form(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_start_page_after_auth(app)

    open_availability_hand_new(app)

    open_arm_lead_detail(app)
