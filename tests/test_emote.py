from emote import get_emote
from paths import ANGRY_GIF, HAPPY_GIF, IDLE_GIF, SAD_GIF


def test_happy_keywords():
    assert get_emote("I'm so happy this works!") == HAPPY_GIF


def test_sad_keywords():
    assert get_emote("This is terrible and sad") == SAD_GIF


def test_angry_keywords():
    assert get_emote("I'm furious about this") == ANGRY_GIF


def test_neutral_fallback():
    assert get_emote("The weather is okay") == IDLE_GIF
