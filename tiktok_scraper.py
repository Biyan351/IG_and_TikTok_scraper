from playwright.sync_api import sync_playwright
import requests
import os

def scrape_tiktok_hashtag(hashtag='fyp', max_videos=5):
    os.makedirs('output/tiktok', exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://www.tiktok.com/tag/{hashtag}')
        page.wait_for_timeout(5000)

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(3000)

        videos = page.query_selector_all("video")
        for idx, vid in enumerate(videos[:max_videos]):
            src = vid.get_attribute("src")
            if src:
                video_data = requests.get(src).content
                with open(f'output/tiktok/video_{idx}.mp4', 'wb') as f:
                    f.write(video_data)
                print(f"[TikTok] Video {idx+1} disimpan.")

        browser.close()
