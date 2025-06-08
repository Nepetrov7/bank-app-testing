from playwright.sync_api import Page


def open_rubles(page: Page, url: str) -> None:
    page.goto(url)
    page.get_by_text("Рубли").click()


def fill_card(page: Page, number: str):
    card_input = page.locator("input[placeholder='0000 0000 0000 0000']")
    card_input.fill(number)
    page.wait_for_timeout(5)
    return card_input


def fill_amount(page: Page, amount: str):
    amount_input = page.locator("input").nth(1)
    amount_input.fill(amount)
    return amount_input


def assert_dialog_message(dialog, expected_symbol):
    assert expected_symbol in dialog.message
    dialog.accept()
