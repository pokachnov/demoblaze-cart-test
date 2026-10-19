import os
from playwright.sync_api import Page, expect

BASE_URL = "https://www.demoblaze.com/"
PRODUCT_NAME = "Samsung galaxy s6"


def test_add_samsung_galaxy_s6_to_cart(page: Page):
    # 1. Открыть главную страницу
    page.goto(BASE_URL)

    # 2. Нажать на товар «Samsung galaxy s6»
    page.get_by_role("link", name=PRODUCT_NAME, exact=True).click()
    expect(page.locator("h2.name")).to_have_text(PRODUCT_NAME)

    # 3. Нажать «Add to cart» и поймать pop-up (JS alert).
    #    Обработчик диалога нужно зарегистрировать ДО клика.
    with page.expect_event("dialog") as dialog_info:
        page.get_by_role("link", name="Add to cart").click()

    # 4. Нажать «OK» в pop-up
    dialog = dialog_info.value
    assert "Product added" in dialog.message
    dialog.accept()

    # 5. Нажать «Cart» в шапке сайта
    page.locator("#cartur").click()

    # Ожидаемый результат: в корзине единственный элемент «Samsung galaxy s6»
    rows = page.locator("#tbodyid tr")
    expect(rows).to_have_count(1)
    expect(rows.first.locator("td").nth(1)).to_have_text(PRODUCT_NAME)
    if os.getenv("PAUSE"):
        page.pause() 
