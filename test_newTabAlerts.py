from playwright.sync_api import Page, expect


def test_handle_popup(page: Page):
    """
    Test case to handle browser JS alerts (confirmations/dialogs).
    """
    # Navigate to the practice automations page
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Register a listener to auto-accept (click OK) on browser dialogs.
    # Note: This listener must be registered BEFORE triggering the dialog.
    page.on("dialog", lambda dialog: dialog.accept())

    # Click the button that triggers the confirm popup
    page.get_by_role("button", name="Confirm").click()


def test_new_tab(page: Page):
    """
    Test case to handle multi-tab redirection, extract dynamic text,
    and assert the parsed email address.
    """
    # Navigate to the login practice page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Use context manager to capture the newly opened tab (popup) triggered by a click
    with page.expect_popup() as new_tab_info:
        # Click the link that opens in a new tab
        page.locator(".blinkingText", has_text="Free Access").click()

    # Resolve the promise to get the Page object representation of the new tab
    new_page = new_tab_info.value

    # Extract the red text block which contains the email sentence
    text = new_page.locator(".red").text_content()

    # Extract the email address from a string pattern like: "... at mentor@rahulshettyacademy.com with ..."
    email = text.split("at")[1].split("with")[0].strip()

    # Verify the extracted email matches the expected value
    assert email == "mentor@rahulshettyacademy.com"


def test_verify_assertions(page: Page):
    """
    Test case to demonstrate the use of assertions in Playwright.
    """
    # Navigate to the login practice page
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()

