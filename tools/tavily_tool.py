from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize the Tavily client
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def tavily_search(query):
    """
    Search Tavily and return formatted search results.
    """

    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        # Limit the snippet length
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(
            f"{i}. **{title}**\n"
            f"   {url}\n"
            f"   {snippet}"
        )

    return "\n\n".join(results)