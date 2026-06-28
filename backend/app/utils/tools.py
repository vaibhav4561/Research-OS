from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """
    Search the web for latest information.
    Useful for current events, facts, research,
    and recent updates.
    """

    response = tavily.search(query = query, num_results = 5 )

    results = []

    for item in response['results']:
        results.append(
            f"Title: {item['title']}\n"
            f"URL: {item['url']}\n"
            f"Content: {item['content'][:300]}\n"
        )

    return "\n\n".join(results)

@tool
def scrape_url(url: str) -> str:
    """
    Scrape the content of a URL.
    Useful for extracting information from specific web pages for deeper reading.
    """

    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        return text[:3000]  
    except Exception as e:
        return f"Error scraping URL: {str(e)}"
    