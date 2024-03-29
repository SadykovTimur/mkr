import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from _pytest.fixtures import FixtureRequest
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.auto_page import AutoPage
from dit.qa.pages.analytics_reports import ReportsPage
from dit.qa.pages.availability_page_old import AvailabilityOldPage
from dit.qa.pages.availability_page_new import AvailabilityNewPage
from dit.qa.pages.arm_lead_detail_page import ArmLeadDetailPage
from dit.qa.pages.availability_sber_page import AvailabilitySberPage
from dit.qa.pages.sber_object_page import SberObjectPage
from dit.qa.pages.sbor_availability_page import SborAvailabilityPage
from dit.qa.pages.state_program_availability_page import StateProgramAvailabilityPage
from dit.qa.pages.state_program_analytic import StateProgramAnalyticPage
from dit.qa.pages.availability_ehd_page import AvailabilityEhdPage
from dit.qa.pages.reports_ehd_page import ReportsEhdPage
from dit.qa.pages.availability_support_page import AvailabilitySupportPage
from dit.qa.pages.analytic_support_page import AnalyticSupportPage


__all__ = [
    'open_start_page',
    'open_auth_form',
    'sign_in',
    'open_start_page_after_auth',
    'open_analytics_page',
    'open_analytics_reports',
    'open_availability_hand_new',
    'open_availability_hand_old'

]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_form(app: Application) -> None:
    with allure.step('Opening Auth form'):
        try:
            page = StartPage(app)
            page.header.login.click()
            page.auth_form.wait_for_loading()

            screenshot_attach(app, 'auth_form')
        except Exception as e:
            screenshot_attach(app, 'auth_form_error')

            raise TimeoutError('Auth form was not loaded') from e


def open_analytics_page(app: Application) -> None:
    with allure.step('Opening analytics page'):
        try:
            page_analytics = AutoPage(app)
            page_analytics.analytics_page()

            screenshot_attach(app, 'analytics_page')
        except Exception as e:
            screenshot_attach(app, 'analytics_page_error')

            raise TimeoutError('Analytics page was not loaded') from e


def open_analytics_reports(app: Application) -> None:
    with allure.step('Opening analytics reports'):
        try:
            page_reports = ReportsPage(app)
            page_reports.analytics_reports_page()
            page_reports.wait_for_loading()

            screenshot_attach(app, 'analytics_reports')
        except Exception as e:
            screenshot_attach(app, 'analytics_reports_error')

            raise TimeoutError('Analytics reports was not loaded') from e


def open_availability_hand_old(app: Application) -> None:
    with allure.step('Opening Availability hand old'):
        try:
            page = AvailabilityOldPage(app)
            page.base_url = 'http://gp.mos.ru/report/'
            page.open()
            page.closeBtn.click()
            page.wait_for_loading()

            screenshot_attach(app, 'availability_hand_old')
        except Exception as e:
            screenshot_attach(app, 'availability_hand_old_error')

            raise TimeoutError('Availability hand old was not loaded') from e


def open_availability_hand_new(app: Application) -> None:
    with allure.step('Opening Availability hand new'):
        try:
            page_hand_new = AvailabilityNewPage(app)
            page_hand_new.arm_lead.click()
            page_hand_new.wait_for_loading()

            screenshot_attach(app, 'availability_hand_new')
        except Exception as e:
            screenshot_attach(app, 'availability_hand_new_error')

            raise TimeoutError('Availability hand new was not loaded') from e


def open_arm_lead_detail(app: Application) -> None:
    with allure.step('Opening Arm lead detail'):
        try:
            page = ArmLeadDetailPage(app)
            page.problem_cards[0].problem_value.click()
            page.wait_for_loading()
            page.open_complex()
            page.wait_for_loading_complex()
            page.open_gp_title()
            page.wait_for_loading_gp_title()

            screenshot_attach(app, 'arm_lead_detail')
        except Exception as e:
            screenshot_attach(app, 'arm_lead_detail_error')

            raise TimeoutError('Arm lead detail was not loaded') from e


def open_availability_sber(app: Application) -> None:
    with allure.step('Opening Availability sber'):
        try:
            page_sber = AvailabilitySberPage(app)
            page_sber.open_data_news()
            page_sber.wait_for_loading()
            page_sber.switch_to_default()

            screenshot_attach(app, 'availability_sber')
        except Exception as e:
            screenshot_attach(app, 'availability_sber_error')

            raise TimeoutError('Availability sber was not loaded') from e


def open_sbor_availability(app: Application) -> None:
    with allure.step('Opening Sbor availability'):
        try:
            page_sbor = SborAvailabilityPage(app)
            page_sbor.open_data_sbor()
            page_sbor.wait_for_loading()

            screenshot_attach(app, 'sbor_availability')
        except Exception as e:
            screenshot_attach(app, 'sbor_availability_error')

            raise TimeoutError('Sbor availability was not loaded') from e


def open_state_program_availability(app: Application) -> None:
    with allure.step('Opening state program availability'):
        try:
            page_availability = StateProgramAvailabilityPage(app)
            page_availability.open_monitoring()
            page_availability.wait_for_loading()
            page_availability.switch_to_default()

            screenshot_attach(app, 'state program')
        except Exception as e:
            screenshot_attach(app, 'state_program_availability_error')

            raise TimeoutError('state program availability was not loaded') from e


def open_state_program_analytic(app: Application) -> None:
    with allure.step('Opening State program analytic'):
        try:
            page_analytic = StateProgramAnalyticPage(app)
            page_analytic.open_report()
            page_analytic.wait_for_loading()
            page_analytic.open_state_program()
            page_analytic.wait_for_loading_state_program()
            page_analytic.open_period()
            page_analytic.wait_for_loading_period()
            page_analytic.open_state_table()
            page_analytic.wait_for_loading_state_program()

            screenshot_attach(app, 'state program analytic')
        except Exception as e:
            screenshot_attach(app, 'state_program_analytic_error')

            raise TimeoutError('State program analytic was not loaded') from e


def open_availability_ehd(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Availability ehd'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['fonts.googleapis.com']})
            app.send_command('Network.enable', {})

        try:
            page_open_ehd = AvailabilityEhdPage(app)
            page_open_ehd.open_ehd()
            page_open_ehd.wait_for_loading()

            screenshot_attach(app, 'availability_ehd')
        except Exception as e:
            screenshot_attach(app, 'availability_ehd_error')

            raise TimeoutError('Availability ehd was not loaded') from e


def open_reports_ehd(app: Application) -> None:
    with allure.step('Opening Reports ehd'):
        try:
            page_ehd = ReportsEhdPage(app)
            page_ehd.open_menu()
            page_ehd.wait_for_loading()
            page_ehd.open_report()
            page_ehd.wait_for_loading_report()

            screenshot_attach(app, 'reports_ehd')
        except Exception as e:
            screenshot_attach(app, 'reports_ehd_error')

            raise TimeoutError('Reports ehd was not loaded') from e


def open_availability_support(app: Application) -> None:
    with allure.step('Opening Availability support'):
        try:
            page_support = AvailabilitySupportPage(app)
            page_support.open_menu()
            page_support.wait_for_loading()
            page_support.switch_to_default()

            screenshot_attach(app, 'availability_support')
        except Exception as e:
            screenshot_attach(app, 'availability_support_error')

            raise TimeoutError('Availability support was not loaded') from e


def open_analytic_support(app: Application) -> None:
    with allure.step('Opening Analytic support'):
        try:
            page = AnalyticSupportPage(app)
            page.open_analytic()
            page.wait_for_loading()
            page.open_social_report()
            page.wait_for_loading_social_report()

            screenshot_attach(app, 'analytic_support')
        except Exception as e:
            screenshot_attach(app, 'analytic_support_error')

            raise TimeoutError('Analytic support was not loaded') from e


def open_sber_object(app: Application) -> None:
    with allure.step('Opening Sber object form'):
        try:
            page_sber = SberObjectPage(app)
            page_sber.open_object()
            page_sber.wait_for_loading()
            page_sber.open_apply()
            page_sber.wait_for_loading_object()

            screenshot_attach(app, 'sber_object')
        except Exception as e:
            screenshot_attach(app, 'sber_object_error')

            raise TimeoutError('Sber object was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app).auth_form

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_start_page_after_auth(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            AutoPage(app).wait_for_loading(True)

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e
