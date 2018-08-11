class UserServiceException(Exception):

    def __init__(self, exception, message, developer_message=None, status_code=None):
        self.exception = exception
        self.message = str(message)
        self.developer_message=developer_message
        self.status_code = status_code