
import requests 

# make an API call and store the response 

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

# Examing the first repo 

# repo_dict = repo_dicts[0] 
# print(f"\nKeys: {len(repo_dict)}") 

# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")


# Summarizing the Top repositories 

for repo_dict in repo_dicts: 
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}") 
    print(f"Description: {repo_dict['description']}")

# Monitoring API rate limits 
# Most API's are rate limited which means there's a limit to how many requests you can make in a certain amount of time 
# To see if you are approaching github's limit enter https://api.github.com/rate_limit

