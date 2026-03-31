from playwright.sync_api import sync_playwright

ORIGIN = "NYP"
DESTINATION = "BOS"
DATE = "04/15/2026"

def get_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False so you can watch it
        page = browser.new_page()
        
        url = f"https://www.amtrak.com/tickets/depart/{ORIGIN}/to/{DESTINATION}/{DATE}/1/seat/United+States"
        print(f"Going to: {url}")
        page.goto(url, wait_until="networkidle", timeout=60000)
        
        # take a screenshot so we can see what loaded
        page.screenshot(path="amtrak.png")
        print("Screenshot saved as amtrak.png")
        
        browser.close()

get_prices()