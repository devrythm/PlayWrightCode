from playwright.sync_api import Page


def test_handle_popup(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()


def test_new_tab(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newTab:
        page.locator(".blinkingText", has_text="Free Access").click()
        newPage = newTab.value
        text = newPage.locator(".red").text_content()
        email = text.split("at")
        email = email[1].strip().split("with")
        assert email[0].strip() == "mentor@rahulshettyacademy.com"