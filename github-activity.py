import sys
import urllib.request
import urllib.error
import json


def fetch_github_activity(username):
    """
    Fetch recent GitHub activity for a given username.

    Args:
        username (str): GitHub username to fetch activity for

    Returns:
        list: List of recent GitHub activity events
    """
    try:
        # Construct the GitHub API URL
        url = f"https://api.github.com/users/{username}/events"

        # Create a request with a User-Agent header (required by GitHub API)
        req = urllib.request.Request(url, headers={"User-Agent": "GitHub-Activity-CLI"})

        # Open the URL and read the response
        with urllib.request.urlopen(req) as response:
            data = response.read()
            events = json.loads(data)
            return events

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Username '{username}' not found.")
        elif e.code == 403:
            print("Error: API rate limit exceeded. Please try again later.")
        else:
            print(f"HTTP Error {e.code}: {e.reason}")
        sys.exit(1)

    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
        sys.exit(1)

    except json.JSONDecodeError:
        print("Error: Unable to parse GitHub API response.")
        sys.exit(1)


def format_event(event):
    """
    Format a single GitHub event into a human-readable string.

    Args:
        event (dict): GitHub event dictionary

    Returns:
        str: Formatted event description
    """
    event_type = event.get("type", "Unknown Event")
    repo = event.get("repo", {}).get("name", "Unknown Repository")

    if event_type == "PushEvent":
        commit_count = len(event.get("payload", {}).get("commits", []))
        return f"- Pushed {commit_count} commit{'s' if commit_count != 1 else ''} to {repo}"

    elif event_type == "CreateEvent":
        ref_type = event.get("payload", {}).get("ref_type", "unknown")
        ref_name = event.get("payload", {}).get("ref", "unknown")
        return f"- Created a new {ref_type} '{ref_name}' in {repo}"

    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action", "unknown")
        issue_title = event.get("payload", {}).get("issue", {}).get("title", "Untitled")
        return f"- {action.capitalize()} an issue '{issue_title}' in {repo}"

    elif event_type == "PullRequestEvent":
        action = event.get("payload", {}).get("action", "unknown")
        pr_title = (
            event.get("payload", {}).get("pull_request", {}).get("title", "Untitled")
        )
        return f"- {action.capitalize()} a pull request '{pr_title}' in {repo}"

    elif event_type == "WatchEvent":
        return f"- Starred {repo}"

    return f"- {event_type} in {repo}"


def main():
    """
    Main function to run the GitHub Activity CLI.
    """
    # Check if username is provided
    if len(sys.argv) < 2:
        print("Usage: python github-activity.py <username>")
        sys.exit(1)

    # Get username from command line argument
    username = sys.argv[1]

    # Fetch GitHub activity
    events = fetch_github_activity(username)

    # Print header
    print(f"Recent GitHub Activity for {username}:")

    # Print formatted events (limit to first 10)
    for event in events[:10]:
        print(format_event(event))


if __name__ == "__main__":
    main()
