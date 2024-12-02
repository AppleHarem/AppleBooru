class WikiPages:
    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """
        Search Wiki pages.

        params:
        - title: Keyword for searching the title
        - body: Keyword for searching the body text
        - other_names: Other names
        - is_deleted: Whether the page is deleted (True/False)
        - is_locked: Whether the page is locked (True/False)
        - category_name: Category name
        - tag: Tag
        - artist: Artist
        - dtext_links: DText links
        - body_matches: Fuzzy match for body text
        - title_normalize: Normalized title match
        - other_names_match: Fuzzy match for other names
        - linked_to: Pages linked to other titles
        - not_linked_to: Pages not linked to other titles
        - hide_deleted: Whether to hide deleted pages (True/False)
        - other_names_present: Whether other names are present (True/False)
        - limit: Maximum number of results per page (default 10)
        - page: Page number (default 1)
        - order: Sorting method (default "updated_at")
        - only: Fields to return, comma-separated (e.g., "id,title,created_at")

        return:
        - List of posts
        """

        search_fields = {
            "title": "search[title]",
            "body": "search[body]",
            "other_names": "search[other_names]",
            "is_deleted": "search[is_deleted]",
            "is_locked": "search[is_locked]",
            "category_name": "search[category_name]",
            "tag": "search[tag]",
            "artist": "search[artist]",
            "dtext_links": "search[dtext_links]",
            "body_matches": "search[body_matches]",
            "title_normalize": "search[title_normalize]",
            "other_names_match": "search[other_names_match]",
            "linked_to": "search[linked_to]",
            "not_linked_to": "search[not_linked_to]",
            "hide_deleted": "search[is_deleted]",
            "other_names_present": "search[other_names_present]",
        }

        # 固定参数
        params = {
            "limit": kwargs.get("limit", 10),
            "page": kwargs.get("page", 1),
            "order": kwargs.get("order", "updated_at"),
            "only": ",".join(kwargs.get("only")) if isinstance(kwargs.get("only"), list) else kwargs.get("only")
        }

        for key, api_param in search_fields.items():
            if key in kwargs and kwargs[key] is not None:
                value = kwargs[key]

                if isinstance(value, bool):
                    value = str(value).lower()

                if key == "hide_deleted" and value:
                    value = "false"
                params[api_param] = value

        response = self.client._request("GET", "/wiki_pages.json", params)
        return response

    def get(self, page_id: int):
        """
        Get post details

        params:
        - post_id: Wiki page id (int)

        return:
        - Post details
        """
        response = self.client._request("GET", f"/wiki_pages/{page_id}.json", {})
        return response.json()
