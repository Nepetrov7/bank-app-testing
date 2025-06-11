import pytest
from playwright.sync_api import Page

from helper_functions import open_rubles, fill_card, fill_amount, assert_dialog_message


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/23")
def test_negative_balance(page: Page):
    page.goto("http://localhost:8000/?balance=-38000")
    balance = page.locator("#rub-sum").inner_text()
    assert "-" not in balance


def test_commission_for_100(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "100")
    commission = page.locator("#comission").inner_text()
    assert commission == "10"


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/26")
def test_invalid_card_number(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1111 1111 1111 1111")
    page.get_by_role("button", name="Перевести").click()
    error = page.locator(".error-message")
    error.wait_for(timeout=5)
    assert "Неверный номер карты" in error.inner_text()


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/27")
def test_cyrillic_input(page: Page):
    page.goto("http://localhost:8000/?reserved=восемьдесят")
    reserved = page.locator("#rub-reserved").inner_text()
    assert reserved.isdigit()


def test_currency_selection(page: Page, app_url: str):
    page.goto(app_url)
    page.get_by_text("Доллары").click()
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "50")
    page.once("dialog", lambda dialog: assert_dialog_message(dialog, "$"))
    page.get_by_role("button", name="Перевести").click()
