from eztts.adapters import APIAdapter
import requests

class FTTSAdapter(APIAdapter):
    """
    An adapter for the fromtexttospeech.com API.
    """

    # LANGUAGES structure:
    #  key: common language name
    #  value: adapter specific language name
    LANGUAGES = {
        "English": "US English",
        "US English": "US English",
        "UK English": "British English",
        "French": "French",
        "Spanish": "Spanish",
        "German": "German",
    }

    # VOICES structure:
    #  key: voice name
    #  value: (common language name, adapter specific voice name)
    VOICES = {
        # US English voices
        "Alice": ("US English", "IVONA Kimberly22"),
        "Daisy": ("US English", "IVONA Salli22"),
        "George": ("US English", "IVONA Joey22"),
        "Jenna": ("US English", "IVONA Jennifer22"),
        "John": ("US English", "IVONA Eric22"),

        # UK English voices
        "Emma": ("UK English", "IVONA Amy22 (UK English)"),
        "Harry": ("UK English", "IVONA Brian22 (UK English)"),

        # French voices
        "Jade": ("French", "IVONA CΘline22 (French)"),
        "Gabriel": ("French", "IVONA Mathieu22 (French)"),

        # Spanish voices
        "Isabella": ("Spanish", "IVONA Conchita22 (Spanish [Modern])"),
        "Mateo": ("Spanish", "IVONA Enrique22 (Spanish [Modern])"),

        # German voices
        "Michael": ("German", "IVONA Hans22 (German)"),
        "Nadine": ("German", "IVONA Marlene22 (German)"),
    }
    
    # SPEEDS structure:
    #  key: common speed name
    #  value: adapter specific speed name
    SPEEDS = {
        "slow": -1,
        "medium": 0,
        "fast": 1,
        "very fast": 2,
    }


    DEFAULT_SPEED = "medium"
    DEFAULT_VOICE = "Alice"

    
    def generate_tts(self, text: str) -> None:
        """
        Generate TTS.
        """
        # Everything needed in the payload:
        #  text
        #  voice
        #  language
        #  speed

        # The adapter specific data for the chosen config is automatically set by the superclass.
        # This data is also automatically encoded to support url encoding.


        if self._debug:
            print("Encoding request data...")


        # Encode the text
        encoded_text = self._url_encode(text)

        # Now we can build the payload
        payload = f"""input_text={encoded_text}
                language={self._encoded_language}
                voice={self._encoded_voice}
                speed={self._encoded_speed}
                action=process_text"""

        # Now replace all new lines with "&"
        payload = payload.replace("\n", "&")
        
        # Now get rid of all spaces
        payload = payload.replace(" ", "")


        if self._debug:
            print("Setting up headers...")

        # The payload is now ready. Set up our headers for the request.
        # I don't know  much about headers. These were all just grabbed from inspect element in Chrome, and Insomnia.
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

        url = "http://www.fromtexttospeech.com/"


        if self._debug:
            # print("Logging payload...")
            # with open("payload.txt", "w") as f:
            #     f.write(payload)
            print("Sending request...")

        # Now make the request
        self.__response = requests.request("POST", url, data=payload, headers=headers)

        if self._debug:
            print("Response received.")


    def save_tts(self, filename: str) -> None:
        """
        Save TTS to file.
        """
        if self._debug:
            print("Saving TTS to file...")
            print("Getting audio location...")

        # In the response.text, find the source tag with the mp3 audio
        try:
            audio_src = self.__response.text.split("<source src=\"")[1].split("\"")[0]
        # If it is an index error, this is probably because src= uses single quotes instead of double quotes
        except IndexError:
            audio_src = self.__response.text.split("<source src='")[1].split("'")[0]


        if self._debug:
            print("Downloading audio...")

        # Use requests to get the audio at the src url, which is a local url on the server
        audio_response = requests.get("http://www.fromtexttospeech.com" + audio_src)


        if self._debug:
            print("Writing audio to file...")

        # Save audio to a file as mp3
        with open(filename, "wb") as f:
            f.write(audio_response.content)

        if self._debug:
            print("Audio saved.")