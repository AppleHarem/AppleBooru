class AppleBooruError(Exception):
    def __init__(self, message=None, details=None):
        self.message = message if message else "An unknown error occurred."
        super().__init__(self.message)
        self.details = details


class APIError(AppleBooruError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "API processing error.", details)


class AuthenticationError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Authentication failed.", details)


class PermissionError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Access denied. Check permissions.", details)


class NotFoundError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Resource not found.", details)


class RateLimitError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "User is throttled. Try again later.", details)


class ServerError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Internal server error.", details)


class BadRequestError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "The given parameters could not be parsed.", details)


class PaginationLimitError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Pagination limit exceeded.", details)


class InvalidRecordError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Record could not be saved.", details)


class LockedError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "The resource is locked and cannot be modified.", details)


class AlreadyExistsError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Resource already exists.", details)


class InvalidParametersError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "The given parameters were invalid.", details)


class BadGatewayError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Server cannot currently handle the request. Try again later.", details)


class ServiceUnavailableError(APIError):
    def __init__(self, message=None, details=None):
        super().__init__(message or "Server is currently unavailable. Try again later.", details)