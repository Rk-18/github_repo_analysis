import requests

def analyze_repositories(url):
    _, _, _, username = url.split("/")

    api_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(api_url)

    if response.status_code == 200:
        repositories = response.json()

        for repository in repositories:
            repository_name = repository["name"]
            repository_url = repository["html_url"]
            print(f"Analyzing repository: {repository_name}")
            analyze_repository(repository_url)
            print("\n")
    else:
        print("Failed to fetch user repositories.")

def analyze_repository(url):
    _, _, _, username, repository = url.split("/")

    api_url = f"https://api.github.com/repos/{username}/{repository}"
    response = requests.get(api_url)

    if response.status_code == 200:
        repository_info = response.json()

        name = repository_info["name"]
        description = repository_info["description"]
        stars = repository_info["stargazers_count"]
        forks = repository_info["forks_count"]
        issues = repository_info["open_issues_count"]

        print("Repository Information:")
        print(f"Name: {name}")
        print(f"Description: {description}")
        print(f"Stars: {stars}")
        print(f"Forks: {forks}")
        print(f"Issues: {issues}")
    else:
        print("Failed to fetch repository information.")

# Example usage
user_url = "https://github.com/NancyDutta"  # Replace with the user's URL you want to analyze
analyze_repositories(user_url)
