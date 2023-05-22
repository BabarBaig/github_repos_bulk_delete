""" Not sure what this does """
import requests

# Set your personal access token and username
TOKEN = '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'
USERNAME = 'BabarBaig'

def github_repo_delete_bulk():
    """ bulk delete github repos.  Prompt before each delete """

    # Fetch a list of repositories
    url = f"https://api.github.com/users/{USERNAME}/repos"
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers, timeout=20)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch repositories. Error: {response.status_code}: {response.text}")
        return

    repositories = response.json()

    # Filter the list of repositories based on your criteria
    repositories_to_delete = [repo for repo in repositories if 'aa' in repo['name']]

    # Delete the repositories
    for repo in repositories_to_delete:
        repo_name = repo['name']
        delete_url = f'https://api.github.com/repos/{USERNAME}/{repo_name}'
        question = f"Delete [{delete_url} ?]"
        resp = input(question)
        print(f'resp: {resp}')
        if resp == 'q':
            print('Goodbye!')
            break
        if resp == 'n':
            continue
        delete_response = requests.delete(delete_url, headers=headers, timeout=10)

        if delete_response.status_code == 204:
            print(f"Repository '{repo_name}' deleted successfully.")
        else:
            print(f"Failed to delete repository '{repo_name}'. Error: {delete_response.text}")

github_repo_delete_bulk()
