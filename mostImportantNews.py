import requests
from bs4 import BeautifulSoup

news_sources = {
    "CNN": "https://www.cnn.com/",
    "BBC News": "https://www.bbc.com/news",
    "New York Times": "https://www.nytimes.com/",
    "Washington Post": "https://www.washingtonpost.com/",
    "Fox News": "https://www.foxnews.com/",
    "Reuters": "https://www.reuters.com/",
    "AP": "https://apnews.com/",
    "NBC News": "https://www.nbcnews.com/",
}

html_content = "<html><head><title>Top Headlines</title></head><body>"
for source, url in news_sources.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []
    for h in soup.find_all("h2"):
        headline = h.get_text().strip()
        link = h.find("a").get("href") if h.find("a") else ""
        headlines.append((headline, link))

    html_content += f"<h2>{source} Headlines</h2>"
    for i, (headline, link) in enumerate(headlines[:10]):
        if link:
            html_content += f"<p>{i + 1}. <a href='{link}'>{headline}</a></p>"
        else:
            html_content += f"<p>{i + 1}. {headline}</p>"

html_content += "</body></html>"

with open("headlines.html", "w") as file:
    file.write(html_content)
