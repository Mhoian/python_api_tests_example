class ResponseModel:
    def __init__(self, http_status: int, content: dict, text: str):
        self.http_status = http_status
        self.content = content
        self.text = text

