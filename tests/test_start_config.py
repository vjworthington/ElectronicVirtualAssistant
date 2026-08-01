# tests/test_start_config.py
from unittest.mock import mock_open, patch

import pytest

from start import EVA, initialize_client, load_config


class TestLoadConfig:
    def test_load_config_valid(self):
        content = "API_KEY=test-key\nMODEL=gpt-4o-mini\nTOKENS=100\n"
        with patch("builtins.open", mock_open(read_data=content)):
            config = load_config()
        assert config == {"API_KEY": "test-key", "MODEL": "gpt-4o-mini", "TOKENS": "100"}

    def test_load_config_skips_empty_lines(self):
        content = "API_KEY=test-key\n\nMODEL=gpt-4o-mini\n"
        with patch("builtins.open", mock_open(read_data=content)):
            config = load_config()
        assert len(config) == 2

    def test_load_config_missing_file(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with pytest.raises(FileNotFoundError):
                load_config()


class TestInitializeClient:
    def test_initialize_client_success(self, monkeypatch):
        mock_config = {"API_KEY": "test-key", "MODEL": "gpt-4o-mini", "TOKENS": "100"}
        monkeypatch.setattr("start.load_config", lambda: mock_config)

        with patch("start.OpenAI") as mock_openai:
            initialize_client()
            mock_openai.assert_called_once_with(
                api_key="test-key", base_url="https://openrouter.ai/api/v1"
            )


def test_initialize_client_file_not_found(monkeypatch, caplog):
    def raise_fnf():
        raise FileNotFoundError("config.txt not found")

    monkeypatch.setattr("start.load_config", raise_fnf)
    initialize_client()
    assert "config.txt not found" in caplog.text


class TestEVA:
    def test_eva_success(self, monkeypatch):
        # Reuse your existing mock pattern
        class FakeResponse:
            choices = [
                type("obj", (object,), {"message": type("obj", (object,), {"content": "Hello!"})})()
            ]

        class FakeCompletions:
            @staticmethod
            def create(**kwargs):
                return FakeResponse()

        class FakeClient:
            chat = type("obj", (object,), {"completions": FakeCompletions()})

        monkeypatch.setattr("start.client", FakeClient())
        monkeypatch.setattr("start.MODEL_NAME", "test-model")
        monkeypatch.setattr("start.TOKENS", 100)

        response = EVA("test prompt")
        assert response == "Hello!"

    def test_eva_client_none(self, monkeypatch):
        monkeypatch.setattr("start.client", None)
        response = EVA("test")
        assert response == "Configuration error."

    def test_eva_exception(self, monkeypatch, caplog):
        class FakeClient:
            chat = type(
                "obj",
                (object,),
                {
                    "completions": type(
                        "obj",
                        (object,),
                        {
                            "create": staticmethod(
                                lambda **kwargs: (_ for _ in ()).throw(Exception("API down"))
                            )
                        },
                    )
                },
            )

        monkeypatch.setattr("start.client", FakeClient())
        monkeypatch.setattr("start.MODEL_NAME", "test")
        monkeypatch.setattr("start.TOKENS", 100)

        response = EVA("test")
        assert response == "Error. Please try again."
        assert "An error occured" in caplog.text
