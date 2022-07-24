import requests
from bs4 import BeautifulSoup
import urllib.parse

class Voice:
    """
    Access with Voices.{language}.{voice}

    Supported voices:
        EnglishUS:
            ALICE
            DAISY
            GEORGE
            JENNA
            JOHN

        EnglishUK:
            EMMA
            HARRY
    """
    class EnglishUS:
        ALICE = "IVONA Kimberly22"
        DAISY = "IVONA Salli22"
        GEORGE = "IVONA Joey22"
        JENNA = "IVONA Jennifer22"
        JOHN = "IVONA Eric22"

    class EnglishUK:
        EMMA = "IVONA Amy22 (UK English)"
        HARRY = "IVONA Brian22 (UK English)"

class Speed:
    """
    Supported speeds:
        SLOW
        MEDIUM
        FAST
        VERY_FAST
    """
    SLOW = -1
    MEDIUM = 0
    FAST = 1
    VERY_FAST = 2

class Language:
    """
    Supported languages:
        ENGLISH_US
    """
    ENGLISH_US = "US English"
    ENGLISH_BRITISH = "British English"

def save_tts_mp3(text: str, filename: str, voice: str=Voice.EnglishUS.ALICE, language: str=Language.ENGLISH_US, speed: int=Speed.MEDIUM, debug: bool=False) -> None:
    if debug:
        print("Encoding request data...")

    # Encode the text to text that can be used in the url
    encoded_text = urllib.parse.quote(text)

    encoded_voice = urllib.parse.quote(voice)
    encoded_language = urllib.parse.quote(language)
    encoded_speed = urllib.parse.quote(str(speed))



    if debug:
        print("Generating request...")

    url = "http://www.fromtexttospeech.com/"

    payload = f"input_text={encoded_text}&language={encoded_language}&voice={encoded_voice}&speed={encoded_speed}&action=process_text"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://www.fromtexttospeech.com",
        "Referer": "http://www.fromtexttospeech.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    if debug:
        print("Sending request and awaiting response...")

    response = requests.request("POST", url, data=payload, headers=headers)

    if debug:
        print("Response received.")
        print("Interpreting response...")

        # save response.text as html doc
        with open("tts_debug.html", "w") as f:
            f.write(response.text)

    # Load the html into BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    if debug:
        print("Retrieving audio url...")

    # Get the source tag of the audio
    audio_tag = soup.find("source")

    # Get the value of src attribute
    audio_src = audio_tag.get("src")

    if debug:
        print("Downloading audio file...")

    # Use requests to get the audio at the src url, which is a local url on the server
    audio_response = requests.get("http://www.fromtexttospeech.com" + audio_src)

    if debug:
        print("Saving audio file as " + filename + "...")

    # Save audio to a file as mp3
    with open(filename, "wb") as f:
        f.write(audio_response.content)

    if debug:
        print("Done.")


if __name__ == "__main__":
    text = """
    Hello there! My name is Henry, and I am a British person who can read whatever you type.
    My API is slow, but you can request as much as you want!
    """
    text = text.strip()

    fileout = "tts.mp3"

    voice = Voice.EnglishUK.HARRY

    language = Language.ENGLISH_BRITISH

    speed = Speed.MEDIUM

    save_tts_mp3(text, fileout, voice=voice, language=language, speed=speed, debug=True)