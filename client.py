import requests
from .errors import *
from .endpoints import Posts, WikiPages


class AppleBooruClient:
    _BASE_URL = "https://danbooru.donmai.us"

    def __init__(self, api_key: str, username: str):
        self._api_key = api_key
        self._username = username
        self._headers = {
            "Authorization": f"Basic {self._encode_credentials()}",
        }
        self._validate_client()
        self.posts = Posts(self)
        self.wiki_pages = WikiPages(self)

    def _encode_credentials(self) -> str:
        import base64
        return base64.b64encode(f"{self._username}:{self._api_key}".encode()).decode()

    def _validate_client(self):
        response = self._request("GET", "/profile.json")
        if response.get("error"):
            raise AuthenticationError(f"Invalid username or api_key - {response['message']}")

        self.user_info = {
            "user_id": response.get("id"),
            "username": response.get("name"),
            "last_logged_in_at": response.get("last_logged_in_at"),
        }

    def _request(self, method: str, endpoint: str, params=None):
        url = f"{self._BASE_URL}{endpoint}"
        params = params or {}

        try:
            response = requests.request(method, url, headers=self._headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            self._handle_request_exception(e)

    def _handle_request_exception(self, exception):
        if isinstance(exception, requests.HTTPError):
            status_code = exception.response.status_code
            error_class = self._error_map.get(status_code)
            if error_class:
                raise error_class(exception.response.text) from exception
            else:
                raise
        else:
            raise

    _error_map = {
        400: BadRequestError,
        401: AuthenticationError,
        403: PermissionError,
        404: NotFoundError,
        410: PaginationLimitError,
        420: InvalidRecordError,
        422: LockedError,
        423: AlreadyExistsError,
        424: InvalidParametersError,
        429: RateLimitError,
        500: ServerError,
        502: BadGatewayError,
        503: ServiceUnavailableError,
    }  # just for api
