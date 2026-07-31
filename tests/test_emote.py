from emote import get_emote

class TestEmoteClassification:
    def test_happy_keywords(self):
        assert get_emote("I'm so happy this works!") == "happy"

    def test_sad_keywords(self):
        assert get_emote("This is terrible and sad") == "sad"

    def test_angry_keywords(self):
        assert get_emote("I'm furious about this") == "angry"

    def test_neutral_fallback(self):
        assert get_emote("The weather is okay") == "idle"
