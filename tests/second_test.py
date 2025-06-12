import pytest
from playwright.sync_api import Page

from helper_functions import open_rubles, fill_card, fill_amount


@pytest.mark.xfail(reason="Привязать баг ТК 2 1")
def test_reserved_input_validation(page: Page, app_url: str):
    page.goto(app_url.replace("reserved=20001", "reserved=-20001"))
    reserved_text = page.locator("#rub-reserved").inner_text()
    assert "-" not in reserved_text


@pytest.mark.xfail(reason="Привязать баг ТК 2 2")
def test_reserved_string_input(page: Page, app_url: str):
    page.goto(app_url.replace("reserved=20001", "reserved=sdfkkij"))
    reserved_text = page.locator("#rub-reserved").inner_text()
    assert reserved_text.isdigit()


@pytest.mark.xfail(reason="Привязать баг ТК 2 3")
def test_reserve_exceeds_balance(page: Page, app_url: str):
    page.goto(app_url.replace("balance=30000&reserved=20001", "balance=30000&reserved=1000000"))
    balance = int(page.locator("#rub-sum").inner_text().replace("'", ""))
    reserved = int(page.locator("#rub-reserved").inner_text().replace("'", ""))
    assert reserved <= balance


def test_transfer_amount_validation(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    amount_input = fill_amount(page, "abcd")
    assert amount_input.input_value() == ""


def test_commission_calculation(page: Page, app_url: str):
    open_rubles(page, app_url)
    fill_card(page, "1234 5678 9012 3456")
    fill_amount(page, "103")
    commission = page.locator("#comission").inner_text()
    assert commission == "10"
