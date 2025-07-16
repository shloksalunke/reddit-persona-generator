import praw
import os
from dotenv import load_dotenv
load_dotenv()

def scrape_user_content(reddit_username: str, limit: int = 50) -> str:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    try:
        user = reddit.redditor(reddit_username)
        content = []

        for comment in user.comments.new(limit=limit):
            content.append(f"[Comment] {comment.body}")

        for post in user.submissions.new(limit=limit):
            content.append(f"[Post: {post.title}] {post.selftext}")

        return "\n".join(content)

    except Exception as e:
        return f"Error fetching user data: {e}"