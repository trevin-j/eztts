from .. import APIAdapter
from gtts import gTTS

class GTTSAdapter(APIAdapter):
    """
    An adapter for the Google Text-to-Speech API, which depends on the gTTS library.
    """

    # LANGUAGES structure:
    #  key: common language name
    #  value: adapter specific language name
    LANGUAGES = {
        "English": "en|com",
        "US English": "en|com",
        "UK English": "en|co.uk",
        "AU English": "en|com.au",
        "CA English": "en|ca",
        "IN English": "en|co.in",
        "IE English": "en|ie",
        "ZA English": "en|co.za",
        "French": "fr|fr",
        "CA French": "fr|ca",
        "FR French": "fr|fr",
        "Mandarin": "zh-CN|com",
        "Chinese": "zh-CN|com",
        "CN Mandarin": "zh-CN|com",
        "TW Mandarin": "zh-TW|com",
        "Portuguese": "pt|pt",
        "BR Portuguese": "pt|com.br",
        "PT Portuguese": "pt|pt",
        "Spanish": "es|com.mx",
        "MX Spanish": "es|com.mx",
        "ES Spanish": "es|es",
        "US Spanish": "es|com",
    }

    # VOICES structure:
    #  key: voice name
    #  value: (common language name, adapter specific voice name)
    VOICES = {
        "Google": ("English", ""),
        "English Google": ("English", ""),
        "US English Google": ("US English", ""),
        "UK English Google": ("UK English", ""),
        "AU English Google": ("AU English", ""),
        "CA English Google": ("CA English", ""),
        "IN English Google": ("IN English", ""),
        "IE English Google": ("IE English", ""),
        "ZA English Google": ("ZA English", ""),
        "French Google": ("French", ""),
        "CA French Google": ("CA French", ""),
        "FR French Google": ("FR French", ""),
        "Mandarin Google": ("Mandarin", ""),
        "CN Google": ("Chinese", ""),
        "CN Mandarin Google": ("CN Mandarin", ""),
        "TW Mandarin Google": ("TW Mandarin", ""),
        "Portuguese Google": ("Portuguese", ""),
        "BR Portuguese Google": ("BR Portuguese", ""),
        "PT Portuguese Google": ("PT Portuguese", ""),
        "Spanish Google": ("Spanish", ""),
        "MX Spanish Google": ("MX Spanish", ""),
        "ES Spanish Google": ("ES Spanish", ""),
        "US Spanish Google": ("US Spanish", ""),
    }
    
    # SPEEDS structure:
    #  key: common speed name
    #  value: adapter specific speed name
    SPEEDS = {
        "slow": True,
        "medium": False,
    }


    DEFAULT_SPEED = "medium"
    DEFAULT_VOICE = "Google"


    def generate_tts(self, text: str) -> None:
        """
        Generate TTS.
        """
        # Voice doesn't matter for gTTS.
        # Separate self._adapter_specific_language by the "|" character.
        # The first part goes in the lang parameter.
        # The second part goes in the tld parameter.
        # The slow parameter is set to the value of self._adapter_specific_speed.
        if self._debug:
            print("Generating TTS...")
            print("Preparing voice data...")
        tld = self._adapter_specific_language.split("|")[1]
        lang = self._adapter_specific_language.split("|")[0]
        slow = self._adapter_specific_speed

        if self._debug:
            print("Generating TTS...")
        self.__tts = gTTS(text=text, tld=tld, lang=lang, slow=slow)

        if self._debug:
            print("TTS generated.")

    def save_tts(self, filename: str) -> None:
        """
        Save TTS to file.
        """
        if self._debug:
            print("Saving TTS to file: " + filename)
        self.__tts.save(filename)

        if self._debug:
            print("TTS saved.")