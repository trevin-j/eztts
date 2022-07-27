import urllib.parse

class APIAdapter:
    """
    An abstract class for TTS adapters.
    Used to create a generic interface for all the TTS options.
    """

    # For LANGUAGES, VOICES, and SPEEDS, adapters must define them as class constant dictionaries with the following structure:

    # LANGUAGES structure:
    #  key: common language name
    #  value: adapter specific language name
    LANGUAGES = {}

    # VOICES structure:
    #  key: common voice name
    #  value: (common language name, adapter specific voice name)
    VOICES = {}
    
    # SPEEDS structure:
    #  key: common speed name
    #  value: adapter specific speed name
    SPEEDS = {}

    DEFAULT_VOICE = None
    DEFAULT_SPEED = None

    def __init__(self, debug: bool=False):
        """
        Initialize the adapter.
        Calls _setup() on subclass initialization.
        """
        self._debug = debug


        if self._debug:
            print(f"Initializing adapter for {type(self).__name__}...")

        if self._debug:
            print("Configuring default voice...")

        # Set _language, _voice, and _speed to default values (the first option in each dictionary)
        # If adapter hasn't set them, it will guess the defaults
        voice = self.DEFAULT_VOICE
        speed = self.DEFAULT_SPEED
        if voice is None:
            voice = list(self.VOICES.keys())[0]
        if speed is None:
            speed = list(self.SPEEDS.keys())[0]
        self.configure_voice(voice=voice, speed=speed)
        self._setup()

        if self._debug:
            print("Adapter initialized.")


    def _setup(self):
        """
        A method the subclass can implement to set up the adapter if necessary.
        """
        pass

    
    def _take_down(self):
        """
        Implement this method in adapter implementations if necessary.
        It is called  when the adapter is finished.
        Use it to clean up after the adapter.
        """
        pass


    def configure_voice(self, voice: str=None, language: str=None, speed: int=None) -> None:
        """
        Configure the voice.

        If language is specified, it will pick the default voice that goes with that language.
        If voice is specified, it will also automatically configure the language.
        If speed is specified, it will set the speed.

        All three values take their common name as argument, not the adapter specific name.
        """
        if self._debug:
            print("Configuring voice...")
    
        if language is not None:
            self._language = language
            for key, value in self.VOICES.items():
                if language == value[0]:
                    self._voice = key
                    break
        if voice is not None:
            self._voice = voice
            self._language = self.VOICES[self._voice][0]
        if speed is not None:
            self._speed = speed


        if self._debug:
            print(f"Voice configured to {self._voice} in {self._language} at {self._speed} speed.")
            print("Saving adapter specific voice, language, and speed...")

        self._adapter_specific_voice = self.VOICES[self._voice][1]
        try:
            self._adapter_specific_speed = self.SPEEDS[self._speed]
        except KeyError:
            if self.DEFAULT_SPEED is not None:
                self._speed = self.DEFAULT_SPEED
            else:
                self._speed = list(self.SPEEDS.keys())[0]
            self._adapter_specific_speed = self.SPEEDS[self._speed]
        self._adapter_specific_language = self.LANGUAGES[self._language]


        if self._debug:
            print("Encoding adapter specific voice, language, and speed...")

        self._encoded_voice = self._url_encode(self._adapter_specific_voice)
        self._encoded_speed = self._url_encode(self._adapter_specific_speed)
        self._encoded_language = self._url_encode(self._adapter_specific_language)

        if self._debug:
            print("Finished configuring voice.")

    
    def finish(self):
        """
        Clean up after the adapter.
        Implement this method in adapter implementations, 
        and call this method in adapter implementations.
        """
        if self._debug:
            print("Cleaning up after adapter...")

        
        self._take_down()

        if self._debug:
            print("Finished cleaning up.")

    
    def generate_tts(self, text: str) -> None:
        """
        Generate TTS.
        Implement this method in adapter implementations.
        """
        raise NotImplementedError("generate_tts() not implemented")


    def save_tts(self, filename: str) -> None:
        """
        Save TTS to file.
        Implement this method in adapter implementations.
        """
        raise NotImplementedError("save_tts() not implemented")

    
    def get_supported_languages(self) -> list:
        """
        Get a list of supported languages.
        """
        return list(self.LANGUAGES.keys())

    
    def get_supported_voices_by_language(self, language: str) -> list:
        """
        Get a list of supported voices for a language.
        """
        voices = []
        for key, value in self.VOICES.items():
            if language == value[0]:
                voices.append(key)
        return voices

    
    def get_supported_speeds(self) -> list:
        """
        Get a list of supported speeds.
        """
        return list(self.SPEEDS.keys())

    
    def _url_encode(self, text: str) -> str:
        """
        URL encode a string.
        """
        # Convert text to a string in case it isn't already
        text = str(text)
        return urllib.parse.quote(text)


    def __contains__(self, item: str) -> bool:
        """
        Check if a voice/language/speed is included with the adapter.
        All categories are checked because there shouldn't be overlap.
        """
        if item in self.VOICES.keys():
            return True
        if item in self.LANGUAGES.keys():
            return True
        if item in self.SPEEDS.keys():
            return True
        return False