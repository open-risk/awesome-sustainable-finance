import requests

# Replace these variables with your own values
owner = 'your-username-or-org'
repo = 'your-repository-name'
token = 'your-personal-access-token'

# GitHub API URL for contributors
url = f'https://api.github.com/repos/{owner}/{repo}/contributors'

# Set up the headers with the personal access token for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    contributors = response.json()
    number_of_contributors = len(contributors)
    print(f'Number of contributors: {number_of_contributors}')
else:
    print(f'Failed to retrieve contributors: {response.status_code}')
    print(response.json())