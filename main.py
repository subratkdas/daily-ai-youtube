import os
import requests
from google.genai import Client

# Load Gemini API Key
client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Load News API Key
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

def get_trending_topic():
    """Fetch top Indian news headline"""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    article = res.get("articles", [])
    if not article:
        return "India success story"
    headline = article[0].get("title", "India success story")
    return headline

def generate_script(topic):
    """Create 20-sec motivational script using Gemini"""
    prompt = f"Write a viral emotional 20-second motivational YouTube Shorts script inspired by: {topic}. Use short punchy lines. End with a strong line."
    result = client.models.generate_content(
        model="models/gemini-1.0-pro",
        contents=prompt
    )
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
