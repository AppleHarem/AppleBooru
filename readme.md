# AppleBooru

**AppleBooru** is a Python library for interacting with the Danbooru API. 
Provides a simple and easy-to-use interface to help developers access and manipulate posts and wiki pages on Danbooru.

## Key Features

- **Client**: All requests to Danbooru API are through the client.
- **Post API**: Easily get posts.
- **Wiki Page API**: Get wiki pages on Danbooru, support search options and fuzzy.

## Installation

```bash
pip install applebooru
```
Usage Example
```python
from applebooru import AppleBooruClient

# Initialize the client
client = AppleBooruClient(api_key="your_api_key", username="your_username")

# Retrieve posts
posts = client.posts.get_posts(other_names_match='史尔特尔', limit=10)
for post in posts:
    print(post)

# Retrieve wiki pages
wiki_pages = client.wiki_pages.get_wiki_pages(title='surtr_(arknights)', only=['id', 'title'], limit=5)
for page in wiki_pages:
    print(page)
```
## Dependencies
+ Python 3.6+
+ requests

## Target Audience
+ Developers who need to interact with the Danbooru API
+ Users who want to automate management of content on Danbooru

## License
MIT License