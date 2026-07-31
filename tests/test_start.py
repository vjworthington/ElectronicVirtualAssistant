from start import EVA


def test_EVA_response(monkeypatch):
    class FakeMessage:
        content = "Hello, I am EVA."

    class FakeChoice:
        message = FakeMessage()

    class FakeResponse:
        choices = [FakeChoice()]

    class FakeCompletions:
        @staticmethod
        def create(**kwargs):
            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    # Replace the real OpenAI client with the fake one
    monkeypatch.setattr("start.client", FakeClient())

    response = EVA("Hello")

    assert response == "Hello, I am EVA."
