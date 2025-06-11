import pytest
from playwright.sync_api import Page

from helper_functions import open_rubles, fill_card, fill_amount


def test_short_card_number(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 34")
    submit = page.get_by_role("button", name="Перевести")
    assert not submit.is_visible()


@pytest.mark.xfail(reason="Привязать баг ТК 4 2")
def test_negative_transfer(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "-40000")
    submit = page.get_by_role("button", name="Перевести")
    assert not submit.is_visible()


@pytest.mark.xfail(reason="Привязать баг ТК 4 3")
def test_small_amount_commission(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "10")
    commission = page.locator("#comission").inner_text()
    assert commission == "1"


def test_transfer_amount_input_validation(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    amount_input = fill_amount(page, "abc")
    assert amount_input.input_value() == ""


@pytest.mark.xfail(reason="Привязать баг ТК 4 5")
def test_leading_zero_input(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    amount_input = fill_amount(page, "001")
    value = amount_input.input_value()
    assert value == "1"
