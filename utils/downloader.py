import requests
import os

def download_file(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"[✓] Saved: {save_path}")
    except Exception as e:
        print(f"[✗] Failed to download {url}: {e}")
