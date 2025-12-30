import os
import requests
import google.generativeai as genai

# Load Gemini Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_trending_topic():
    url = "https://trends.google.com/trends/api/dailytrends?hl=en-IN&tz=-330&geo=IN"
    response = requests.get(url)
    data = response.text.replace(")]}',", "")
    json_data = response.json() if isinstance(response, dict) else requests.get(url).json()
    data = requests.get(url).text.replace(")]}',", "")
    json_data = requests.get(url).json()
    topic = json_data["default"]["trendingSearchesDays"][0]["trendingSearches"][0]["title"]["query"]
    return topic

def generate_script(topic):
    prompt = f"Write a short 30 second motivational script based on this trending topic: {topic}. Make it inspiring, positive, and suitable for a YouTube short."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    trend = get_trending_topic()
    script = generate_script(trend)
    print("Trending Topic:", trend)
    print("Script:", script)
