from flask import Flask, render_template
import requests
import string

app = Flask(__name__)

API_KEY = "pub_7e4f8339043448b39fad6ccee7f150e8"
BASE_URL = "https://newsdata.io/api/1/latest"

def fetch_by_keyword(q):
    """
    Fetch news for a single keyword.
    Returns a list of articles (dicts), or empty list if error.
    """
    params = {
        "apikey": API_KEY,
        "country": "in",
        "language": "en",
        "q": q
    }
    try:
        r = requests.get(BASE_URL, params=params, timeout=10)
        res = r.json()
        results = res.get("results", [])
        if not isinstance(results, list):
            return []
        return results
    except Exception as e:
        print(f"Error fetching keyword '{q}': {e}")
        return []

def fetch_all_news():
    """
    Fetch news for multiple keywords (a-z) to bypass 10-article limit.
    Removes duplicates based on the 'link' field.
    """
    all_news = []
    used_links = set()

    for letter in string.ascii_lowercase:
        news_list = fetch_by_keyword(letter)
        for n in news_list:
            if isinstance(n, dict):
                link = n.get("link")
                if link and link not in used_links:
                    all_news.append(n)
                    used_links.add(link)

    print(f"Total articles fetched: {len(all_news)}")
    return all_news

@app.route("/")
def home():
    news = fetch_all_news()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)
