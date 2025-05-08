# app/github_service.py

import requests

GITHUB_API_URL = "https://api.github.com/users/TanushriVijay12/repos"

def fetch_github_repos():
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        data = response.json()

        projects = []
        for repo in data:
            projects.append({
                'name': repo['name'],
                'description': repo['description'],
                'url': repo['html_url'],
                'language': repo['language'] or 'Other',
            })

        return projects
    except Exception as e:
        print("GitHub API Error:", e)
        return []
