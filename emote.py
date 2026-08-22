from paths import ANGRY_GIF, HAPPY_GIF, IDLE_GIF, LOVE_GIF, SAD_GIF, SURPRISE_GIF


# Link EVA responses to expressions
def get_emote(response):
    text = response.lower()

    # test keywords for each emotion, will change to more specific keywords later
    happy_keywords = ["happy", "excited", "glad", "pleased", "funny", "optomistic", "inspiring"]
    sad_keywords = [
        "sad",
        "disappointed",
        "regret",
        "insecure",
        "shame",
        "gloomy",
        "depressed",
        "unhappy",
    ]
    angry_keywords = [
        "angry",
        "disgust",
        "dislike",
        "irritated",
        "frustrated",
        "irate",
        "outraged",
        "grumpy",
        "livid",
        "cranky",
    ]
    surprise_keywords = [
        "surprised",
        "shocked",
        "amazed",
        "astonished",
        "impressed",
        "speechless",
        "jolted",
    ]
    love_keywords = [
        "love",
        "adore",
        "cherish",
        "fond",
        "devoted",
        "infatuated",
        "longing",
        "enamored",
        "smitten",
        "irresistible",
    ]

    if any(keyword in text for keyword in happy_keywords):
        return HAPPY_GIF
    elif any(keyword in text for keyword in sad_keywords):
        return SAD_GIF
    elif any(keyword in text for keyword in angry_keywords):
        return ANGRY_GIF
    elif any(keyword in text for keyword in surprise_keywords):
        return SURPRISE_GIF
    elif any(keyword in text for keyword in love_keywords):
        return LOVE_GIF
    else:
        return IDLE_GIF
