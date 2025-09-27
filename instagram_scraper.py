from playwright.sync_api import sync_playwright
import requests
import os

def scrape_instagram_hashtag(hashtag='k3', max_images=10):
    os.makedirs('output/instagram', exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://www.instagram.com/explore/tags/{hashtag}/')
        page.wait_for_timeout(5000)

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(3000)

        images = page.query_selector_all("img")
        for idx, img in enumerate(images[:max_images]):
            src = img.get_attribute("src")
            if src:
                img_data = requests.get(src).content
                with open(f'output/instagram/img_{idx}.jpg', 'wb') as f:
                    f.write(img_data)
                print(f"[Instagram] Gambar {idx+1} disimpan.")

        browser.close()
