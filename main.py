import praw
import re

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    user_agent='my_bot by /u/YOUR_USERNAME'
)

# Define the subreddit to monitor
subreddit = reddit.subreddit('all')  # Monitor all subreddits

# Define the responses
responses = {
    'my': 'Our*, comrade',
    'mine': 'Ours*, comrade'
}

# Define the GitHub repository link
github_link = (
    "\n\n---\n"
    "^(I'm a bot created to remind you of what belongs to who by replacing 'my' with 'our' and 'mine' with 'ours'.) "
    "[^GitHub ^Repository](https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME)"
)

# Stream comments
for comment in subreddit.stream.comments(skip_existing=True):
    try:
        # Check if the keywords are in the comment
        if re.search(r'\bmy\b', comment.body, re.IGNORECASE):
            # Reply to the comment with 'Our* comrade'
            comment.reply(responses['my'] + github_link)
            print(f"Replied to comment {comment.id} with 'Our* comrade'")
        elif re.search(r'\bmine\b', comment.body, re.IGNORECASE):
            # Reply to the comment with 'Ours* comrade'
            comment.reply(responses['mine'] + github_link)
            print(f"Replied to comment {comment.id} with 'Ours* comrade'")
    except Exception as e:
        print(f"Error: {e}")
