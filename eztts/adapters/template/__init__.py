from .. import APIAdapter

class CLASSNAME(APIAdapter):
    """
    An adapter template for TTS adapters.
    """

    # LANGUAGES structure:
    #  key: common language name
    #  value: adapter specific language name
    LANGUAGES = {}

    # VOICES structure:
    #  key: voice name
    #  value: (common language name, adapter specific voice name)
    VOICES = {}
    
    # SPEEDS structure:
    #  key: common speed name
    #  value: adapter specific speed name
    SPEEDS = {}


    DEFAULT_SPEED = None
    DEFAULT_VOICE = None


    def generate_tts(self, text: str) -> None:
        """
        Generate TTS.
        """
        raise NotImplementedError("generate_tts() not implemented")


    def save_tts(self, filename: str) -> None:
        """
        Save TTS to file.
        """
        raise NotImplementedError("save_tts() not implemented")

    
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