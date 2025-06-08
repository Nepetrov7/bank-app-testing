import pytest
from playwright.sync_api import Page

from helper_functions import open_rubles, fill_card, fill_amount


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/14")
def test_card_number_validation(page: Page, app_url: str):
    open_rubles(page, app_url)
    card = fill_card(page, "9999 9999 9999 9999 9")
    value = card.input_value().replace(" ", "")
    assert len(value) <= 16


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/15")
def test_balance_input_validation(page: Page, app_url: str):
    page.goto(app_url.replace("balance=30000", "balance=gdd"))
    balance_text = page.locator("#rub-sum").inner_text()
    assert balance_text.isdigit()


@pytest.mark.xfail(reason="https://github.com/Nepetrov7/bank-app-testing/issues/16")
def test_currency_switch(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "2250")
    page.get_by_role("button", name="Перевести").click()
    page.get_by_text("Доллары").click()
    submit = page.get_by_role("button", name="Перевести")
    assert not submit.is_visible()


def test_card_input_character_validation(page: Page, app_url: str):
    open_rubles(page, app_url)
    card_input = fill_card(page, "abcd")
    assert card_input.input_value() == ""


def test_insufficient_funds(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "288000")
    submit_button = page.get_by_role("button", name="Перевести")
    assert not submit_button.is_visible()
    error_message = page.locator("span").filter(has_text="Недостаточно средств на счете")
    assert error_message.is_visible()
