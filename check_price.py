from playwright.sync_api import sync_playwright

def get_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Loading Wanderu...")
        url = "https://www.wanderu.com/en-us/depart/New%20York%2C%20NY%2C%20US/Boston%2C%20MA%2C%20US/2026-04-15/?donly=true"
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(5000)
        
        page.screenshot(path="wanderu.png")
        print("Screenshot saved")
        
        input("Press Enter to close...")
        browser.close()

get_prices()