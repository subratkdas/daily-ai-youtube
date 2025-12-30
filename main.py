import os
import requests
from google.genai import Client

# Load Gemini Client
client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Load News API Key (required)
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

def get_trending_topic():
    """Fetch top headline from India using NewsAPI"""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    article = res.get("articles", [])
    if not article:
        return "Success story India"
    headline = article[0].get("title", "Success story India")
    return headline

def generate_script(topic):
    """Use Gemini AI to create motivational script"""
    prompt = f"Write a viral motivational 20-second YouTube Shorts script inspired by: {topic}. Use simple English, emotional lines, 1–2 sentences per line, end with strong closing."
   result = client.models.generate_content(model="models/gemini-1.0-pro", contents=prompt)
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
