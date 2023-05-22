import requests

def github_repo_delete_bulk():
    # Set your personal access token and username
    TOKEN = 'YOUR_PERSONAL_ACCESS_TOKEN'
    USERNAME = 'YOUR_GITHUB_USERNAME'

    # Fetch a list of repositories
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(f'https://api.github.com/user/repos', headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        repositories = response.json()

        # Filter the list of repositories based on your criteria
        repositories_to_delete = [repo for repo in repositories if 'filter_condition' in repo['name']]

        # Delete the repositories
        for repo in repositories_to_delete:
            repo_name = repo['name']
            delete_url = f'https://api.github.com/repos/{USERNAME}/{repo_name}'
            delete_response = requests.delete(delete_url, headers=headers)

            if delete_response.status_code == 204:
                print(f"Repository '{repo_name}' deleted successfully.")
            else:
                print(f"Failed to delete repository '{repo_name}'. Error: {delete_response.text}")

    else:
        print(f"Failed to fetch repositories. Error: {response.text}")

print('Hello, world!')
github_repo_delete_bulk()
