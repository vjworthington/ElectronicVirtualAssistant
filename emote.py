from openai import OpenAI
from paths import AVATAR_GIF
from paths import HAPPY_GIF
from paths import SAD_GIF
from paths import ANGRY_GIF
from paths import SURPRISE_GIF
from paths import LOVE_GIF
from paths import IDLE_GIF
import sys


# Link EVA responses to expressions
def get_emote(response):
    text = response.lower()

    # test keywords for each emotion, will change to more specific keywords later
    happy_keywords = ['happy','excited','glad','pleased','funny']
    sad_keywords = ['sad','disappointed','regret','insecure','shame']
    angry_keywords = ['angry','disgust','dislike','irritated','frustrated']
    surprise_keywords = ['surprise','shocked','amazed','astonished','impressed']
    love_keywords = ['love','adore','cherish','fond','devoted']

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