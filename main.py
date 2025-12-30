import os
import requests
import google.generativeai as genai
import json

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_trending_topic():
    url = "https://trends.google.com/trends/api/dailytrends?hl=en-IN&tz=-330&geo=IN"
    res = requests.get(url)
    text = res.text.replace(")]}',", "")   # remove security prefix
    data = json.loads(text)
    topic = data["default"]["trendingSearchesDays"][0]["trendingSearches"][0]["title"]["query"]
    return topic

def generate_script(topic):
    prompt = f"Write a powerful 30-second motivational YouTube Shorts script inspired by this trending topic: {topic}. Make it emotional, short sentences, high-impact."
    model = genai.GenerativeModel("gemini-pro")
    reply = model.generate_content(prompt)
    return reply.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
