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
  - login: The Github user ID (login) of the owner
  - full_name: Full name of the repository
  - description
  - language
  - created_at
  - stargazers_count
  - watchers_count
  - has_projects
  - has_wiki
  - license_name

### Explanation of how the data was scraped

The data was scraped using the GitHub API. The script first fetches users in the specified city with over the specified number of followers. Then, for each user, it fetches up to 500 most recently pushed repositories. The data is then saved to `users.csv` and `repositories.csv` files.

### Most interesting and surprising fact

The most interesting and surprising fact found after analyzing the data is that a significant number of repositories do not have a license specified. This can lead to legal issues for developers who use these repositories without proper understanding of the licensing terms.

### Actionable recommendation for developers

Based on the analysis, it is recommended that developers always specify a license for their repositories. This helps other developers understand the terms under which they can use the code and avoid potential legal issues.
