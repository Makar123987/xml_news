from bs4 import BeautifulSoup
import requests

rss_url = "https://scipost.org/atom/publications/comp-ai"
resp = requests.get(rss_url)
xml_doc = resp.text

soup = BeautifulSoup(xml_doc, 'lxml-xml')

def parse_news():
    news = []
    for entry in soup.find_all('entry'):
        title = entry.title.text if entry.title else ""

        link = entry.link['href'] if entry.link and entry.link.has_attr('href') else ""

        txt_tag = entry.find(['summary', 'content'])
        text = txt_tag.get_text() if txt_tag else ""

        news.append(f" {title} {link}\n {text if text else ''} {'='*100}")

    return news

if __name__ == '__main__':
    print("\n".join(parse_news()))

