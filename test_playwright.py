import time
from playwright.sync_api import Page, expect

def test_playwrite(playwright):
    """
    Test case demonstrating manual control over browser lifecycle.
    Launches Chrome in non-headless mode and navigates to the login page.
    """
    # Explicitly launch a chromium browser instance (headless=False of runs it in headed mode)
    browser = playwright.chromium.launch(headless=False)

    # Create a new isolated browser context (equivalent to an incognito session)
    context = browser.new_context()

    # Open a new tab/page inside that context
    page = context.new_page()

    # Navigate to the target practice login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Note: When pytest finishes, browser/context are closed automatically because of playwright.sync_api


def test_signin_method(page: Page):
    """
    Test case to sign in to the application with valid teacher credentials.
    Can also be used as a setup/helper function by other tests.
    """
    # Navigate directly to the login practice page
    page.goto(url="https://rahulshettyacademy.com/loginpagePractise/")

    # Locate the Username input label and fill it with credential
    page.get_by_label("Username:").fill("rahulshettyacademy")

    # Locate the Password input label and fill it with credential
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    # Select the "Teacher" option from the role dropdown menu
    page.get_by_role("combobox").select_option("teach")

    # Find and click the Sign In submit button
    page.get_by_role("button", name="Sign In").click()


def test_add_to_cart(page: Page):
    """
    Test case to log in, add specific items to the cart,
    and assert that their count is correct on checkout.
    """
    # Re-use the sign-in logic to log in first
    test_signin_method(page)

    # Find the specific product card for 'Samsung Note 8' and click the add button within that card
    product = page.locator("app-card", has_text="Samsung Note 8")
    product.get_by_role("button").click()

    # Alternative locator filter method to find 'Blackberry' and click its button
    page.locator("app-card").filter(has_text="Blackberry").get_by_role("button").click()

    # Click on the Checkout button to view the cart page
    page.get_by_text("Checkout").click()
    time.sleep(2)

    # Assert that there are exactly 2 items inside the checkout list (items with class '.media')
    expect(page.locator(".media")).to_have_count(2)