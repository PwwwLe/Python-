import plotly.express as px
import requests

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转化为字典
response_dict = r.json()
# print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
stars, repo_links = [], []
# print(f"Repositories returned: {len(repo_dicts)}")

# print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    # 将仓库名转换为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    # print(f"Name: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository : {repo_dict['html_url']}")
    # print(f"Created : {repo_dict['created_at']}")
    # print(f"Updated : {repo_dict['updated_at']}")
    # print(f"Description : {repo_dict['description']}")

# 可视化
title = "Github上最多收藏的Python项目"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
