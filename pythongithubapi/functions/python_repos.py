
import requests 
def  repos():
    """This function is responsible for Testing the github repository api and to print reponse data on the terminal for inspection"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort-stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers) 
    print(f"Status code: {r.status_code}") 

    # store API response in a variable 
    response_dict = r.json() 

    # Process results 

    print(response_dict.keys())
    print(f"Total repositories: {response_dict['total_count']}")

    # Explore information about the repositories 
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}") 

    # Summarizing the Top repositories 
    print("\nSelected information about each repository")
    for repo_dict in repo_dicts: 
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}") 
        print(f"Description: {repo_dict['description']}")

repos()


