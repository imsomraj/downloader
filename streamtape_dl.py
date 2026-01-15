import re
import requests
from bs4 import BeautifulSoup

def get_dl_link(url):
    if "/e/" in url:
        url = url.replace("/e/", "/v/")

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36",
        "Referer": "https://streamtape.to/"
    }

    try:
        r = requests.get(url, headers=headers, timeout=15)
        html = r.text

        m = re.search(r"norobotlink'\)\.innerHTML = (.+?);", html)
        if not m:
            return None

        token_match = re.search(r"token=([^&']+)", m.group(1))
        if not token_match:
            return None

        token = token_match.group(1)

        soup = BeautifulSoup(html, "html.parser")
        hidden = soup.find("div", id="ideoooolink")
        if not hidden:
            return None

        return f"https:/{hidden.text}&token={token}&dl=1"

    except Exception:
        return None
