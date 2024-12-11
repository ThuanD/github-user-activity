# GitHub Activity CLI

## Description
A simple command-line interface (CLI) tool to fetch and display recent GitHub activity for a given username using the GitHub API.

_Note: This project is part of the Roadmap Projects: https://roadmap.sh/projects/github-user-activity_

## Features
- Fetch recent GitHub events for a specified user
- Display events in a human-readable format
- Support for various event types including:
    - Push events
    - Create events
    - Issues events
    - Pull Request events
    - Watch events
- Error handling for network and API issues

## Requirements
- Python 3.7+
- No external libraries required

## Installation
1. Clone the repository
2. Ensure you have Python 3.7+ installed

## Usage
```bash
python github-activity.py <github-username>
```

### Example
```bash
python github-activity.py ThuanD
```

## Event Types Supported
- Pushing commits
- Creating repositories, branches, or tags
- Opening/closing issues
- Creating/merging pull requests
- Starring repositories

## Limitations
- Limited to the 10 most recent events
- Relies on GitHub's public events API
- Subject to GitHub API rate limits

## Potential Improvements
- Add caching mechanism
- Implement event type filtering
- Support authentication for more events
- Display more detailed event information

## Error Handling
- Handles network errors
- Provides user-friendly error messages
- Exits gracefully on API or network issues

## License

This project is open-source.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact & Support

Found an issue? Please open a GitHub issue with detailed information.

Project Link: [https://github.com/ThuanD/github-user-activity](https://github.com/ThuanD/github-user-activity)