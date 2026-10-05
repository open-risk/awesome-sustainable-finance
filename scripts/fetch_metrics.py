import requests

repo = "SBTi-finance-tool"
owner = "ScienceBasedTargets"

# GitHub API URL for contributors
url = f'https://api.github.com/repos/{owner}/{repo}/contributors'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    contributors = response.json()
    number_of_contributors = len(contributors)
    print(f'Number of contributors: {number_of_contributors}')
else:
    print(f'Failed to retrieve contributors: {response.status_code}')
    print(response.json())