import time
from playwright.sync_api import Page, expect


def test_playwrite(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

def test_signin_method(page:Page):
    page.goto(url="https://rahulshettyacademy.com/loginpagePractise/")
    #test_playwrite(playwright)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button", name="Sign In").click()
    #time.sleep(5)

def test_add_to_cart(page:Page):
    # Add 2 items in cart and validate if 2 are present in cart
    test_signin_method(page)
    product = page.locator("app-card", has_text="Samsung Note 8")
    product.get_by_role("button").click()
    page.locator("app-card").filter(has_text="Blackberry").get_by_role("button").click()
    page.get_by_text("Checkout").click()
    time.sleep(2)
    expect(page.locator(".media")).to_have_count(2)

