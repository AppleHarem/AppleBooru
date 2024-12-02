class Posts:
    def __init__(self, client):
        self.client = client

    def search(self, tags: str = None, limit: int = 10, page: int = 1, **kwargs):
        """
        Search mode api

        params:
        - tags: Search through tags (string, Optional)
        - limit: Page limit (int, Default 10)
        - page: page number (int, Default 1)
        - kwargs: other params if supported

        return:
        - List of posts
        """
        params = {
            "tags": tags,
            "limit": limit,
            "page": page,
            "only": ",".join(kwargs.get("only")) if isinstance(kwargs.get("only"), list) else kwargs.get("only")
        }

        params = {k: v for k, v in params.items() if v is not None}

        response = self.client._request("GET", "/posts.json", params)
        return response

    def get(self, post_id: int):
        """
        Get post details

        params:
        - post_id: Post id (int)

        return:
        - Post details
        """
        response = self.client._request("GET", f"/posts/{post_id}.json", {})
        return response.json()
