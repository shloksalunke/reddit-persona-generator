import os
from dotenv import load_dotenv
from src.reddit_scraper import scrape_user_content
from src.persona_generator import generate_persona_with_mistral
from src.utils import save_persona_to_file

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

def extract_username_from_url(url: str) -> str:
    return url.rstrip('/').split('/')[-1]

def main():
    if not api_key:
        print("❌ ERROR: MISTRAL_API_KEY not found in environment. Please check your .env file.")
        return

    try:
        url = input("🔗 Enter Reddit user profile URL: ").strip()
        if not url.startswith("https://www.reddit.com/user/"):
            print("❌ Invalid Reddit user URL. It should look like: https://www.reddit.com/user/username/")
            return

        reddit_username = extract_username_from_url(url)
        print(f"🔍 Scraping content for Reddit user: {reddit_username}")
        content = scrape_user_content(reddit_username)

        print("🤖 Generating persona using Mistral AI...")
        persona = generate_persona_with_mistral(content, api_key)

        print("💾 Saving to output file...")
        save_persona_to_file(reddit_username, persona)

        print(f"✅ Done! Output saved to: output/{reddit_username}_persona.txt")

    except Exception as e:
        print(f"❌ Something went wrong: {e}")

if __name__ == "__main__":
    main()
