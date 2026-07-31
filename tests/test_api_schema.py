from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-4o-mini"


class ChatResponse(BaseModel):
    response: str
    emotion: str


def test_request_schema_valid():
    req = ChatRequest(message="hello")
    assert req.message == "hello"
    assert req.model == "gpt-4o-mini"


def test_response_schema_valid():
    resp = ChatResponse(response="Hi!", emotion="happy")
    assert resp.emotion == "happy"
