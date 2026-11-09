import requests
import json
import os
import re
import time

import requests

INPUT_FILE = "outputs/asf.json"
OUTPUT_FILE = "stats.json"

if __name__ == "__main__":

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    for outer_key, inner_dict in data.items():
        for inner_key, value in inner_dict.items():
            if value['host'] == 'github.com' and value['owner']:
                # GitHub API URL for contributors
                repo = value['repo']
                owner = value['owner']
                url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
                # Make the API request
                response = requests.get(url)
                contributors = response.json()
                count = len(contributors)
                results.append({
                    "url": url,
                    "owner": owner,
                    "repo": repo,
                    "contributors": count
                })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved {len(results)} results to {OUTPUT_FILE}")
