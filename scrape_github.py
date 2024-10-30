import requests
import csv

# GitHub API base URL
BASE_URL = "https://api.github.com"

# Function to get users in the specified city with over the specified number of followers
def get_users(city, followers):
    users = []
    page = 1
    while True:
        url = f"{BASE_URL}/search/users?q=location:{city}+followers:>{followers}&page={page}"
        response = requests.get(url)
        data = response.json()
        if "items" not in data:
            break
        users.extend(data["items"])
        if len(data["items"]) < 30:
            break
        page += 1
    return users

# Function to get user details
def get_user_details(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)
    return response.json()

# Function to get repositories of a user
def get_repositories(username):
    repos = []
    page = 1
    while True:
        url = f"{BASE_URL}/users/{username}/repos?page={page}"
        response = requests.get(url)
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

# Function to clean up company names
def clean_company_name(company):
    if company:
        company = company.strip()
        if company.startswith("@"):
            company = company[1:]
        company = company.upper()
    return company

# Function to save users to CSV
def save_users_to_csv(users, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["login", "name", "company", "location", "email", "hireable", "bio", "public_repos", "followers", "following", "created_at"])
        for user in users:
            writer.writerow([
                user["login"],
                user["name"] or "",
                clean_company_name(user["company"]),
                user["location"] or "",
                user["email"] or "",
                user["hireable"] or "",
                user["bio"] or "",
                user["public_repos"],
                user["followers"],
                user["following"],
                user["created_at"]
            ])

# Function to save repositories to CSV
def save_repositories_to_csv(repositories, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["repository name", "description", "language", "created_at", "updated_at", "pushed_at", "stargazers_count", "watchers_count", "forks_count", "open_issues_count"])
        for repo in repositories:
            writer.writerow([
                repo["name"],
                repo["description"] or "",
                repo["language"] or "",
                repo["created_at"],
                repo["updated_at"],
                repo["pushed_at"],
                repo["stargazers_count"],
                repo["watchers_count"],
                repo["forks_count"],
                repo["open_issues_count"]
            ])

# Main function
def main():
    city = "San Francisco"
    followers = 100
    users = get_users(city, followers)
    user_details = [get_user_details(user["login"]) for user in users]
    save_users_to_csv(user_details, "users.csv")
    all_repositories = []
    for user in users:
        repositories = get_repositories(user["login"])
        all_repositories.extend(repositories)
    save_repositories_to_csv(all_repositories, "repositories.csv")

if __name__ == "__main__":
    main()
