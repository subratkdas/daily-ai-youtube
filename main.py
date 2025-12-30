import os
import requests
import feedparser
from google.genai import Client

client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_trending_topic():
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN"
    feed = feedparser.parse(url)
    first_title = feed.entries[0].title
    return first_title

def generate_script(topic):
    prompt = f"Write a powerful viral 25-second motivational short script inspired by this trending Indian news topic: {topic}. Make it punchy, emotional, fast-paced, 1–2 sentence per line."
    result = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
