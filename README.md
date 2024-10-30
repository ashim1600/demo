# demo

## Scraping Users and Repositories using the GitHub API

This project scrapes users in the city of ${city} with over ${followers} followers and their repositories using the GitHub API. The data is saved in `users.csv` and `repositories.csv` files.

### Instructions

1. Install the required libraries:
   ```
   pip install requests
   ```

2. Run the script:
   ```
   python scrape_github.py
   ```

### Files

- `users.csv`: Contains the following fields about each user:
  - login: Their Github user ID
  - name: Their full name
  - company: The company they work at. Clean up company names. At least make sure:
    - They're trimmed of whitespace
    - Leading @ symbol is stripped (Note: ONLY the first one is stripped)
    - They are converted to UPPERCASE
  - location: The city they are in
  - email: Their email address
  - hireable: Whether they are open to being hired
  - bio: A short bio about them
  - public_repos: The number of public repositories they have
  - followers: The number of followers they have
  - following: The number of people they are following
  - created_at: When they joined Github

- `repositories.csv`: Contains the following fields about each repository:
  - repository name
  - description
  - language
  - created_at
  - updated_at
  - pushed_at
  - stargazers_count
  - watchers_count
  - forks_count
  - open_issues_count
