from .adapters.api_adapter import APIAdapter

valid_adapters = []

from .adapters.ftts_adapter import FTTSAdapter
valid_adapters.append(FTTSAdapter)

try:
    from .adapters.gtts_adapter import GTTSAdapter
    valid_adapters.append(GTTSAdapter)
except ImportError:
    pass


def tts(p_text: str,
        p_filename: str,
        p_adapter: APIAdapter=None,
        p_voice_name: str=None,
        p_speed: str=None,
        p_language: str=None,
        debug: bool=False) -> None:
    """
    Generate text to speech and save it to a file.

    Args:
    Required:
        text: The text to get TTS from.
        filename: The output mp3 file. Include ".mp3"
    Optional:
        adapter: The adapter to use, if a specific adapter is desired.
        voice_name: The name of the voice to use. Uses default if not passed.
        speed: The speed to read the text. Uses default if not passed.
        language: The language of the text. Defaults to English US.
        debug: Whether or not to print debug messages.

    Specifying a voice name will automatically set the language and pick the adapter
    that has the voice. If multiple adapters have that voice, it will use the first one
    it finds. Specify an adapter to override the default adapter.

    Specifying a language and not a voice will pick a valid voice and adapter for that language.

    Being too specific with language, voice, and adapter will result in an error if that
    configuration does not exist.

    Speed is independent of language and voice. If not specified, it will be set to the default.
    If the adapter does not support the selected speed, it will override to the default.
    """
    adapter = None
    adapter_instance = None

    if p_adapter is not None:
        if not issubclass(p_adapter, APIAdapter):
            raise TypeError("Adapter must be an instance of APIAdapter")

        temp_adapter = p_adapter()
        if p_voice_name is not None:
            if not p_voice_name in temp_adapter:
                raise ValueError("Specified voice name not found in specified adapter")
        if p_language is not None:
            if not p_language in temp_adapter:
                raise ValueError("Specified language not found in specified adapter")

        adapter = p_adapter


    elif p_voice_name is not None and p_language is not None:
        # Loop through and see if there is a valid adapter for the language and voice
        for i_adapter in valid_adapters:
            # Instance temporary adapter so we can check if it has the voice
            temp_adapter = i_adapter()
            # If the adapter has the voice and language, use it
            if p_voice_name in temp_adapter and \
                    p_language in temp_adapter:
                adapter = i_adapter
                break
        # If we didn't find a valid adapter, raise an error
        if not adapter:
            raise ValueError("Language and voice combination not supported by any adapters.")
    
    elif p_voice_name is not None:
        for i_adapter in valid_adapters:
            temp_adapter = i_adapter()
            if p_voice_name in temp_adapter:
                adapter = i_adapter
                break
        if not adapter:
            raise ValueError("Voice not supported by any adapters.")

    elif p_language is not None:
        for i_adapter in valid_adapters:
            temp_adapter = i_adapter()
            if p_language in temp_adapter:
                adapter = i_adapter
                break
        if not adapter:
            raise ValueError("Language not supported by any adapters.")

    else:
        # If no adapter or language is specified, use the first adapter
        adapter = valid_adapters[0]


    tts_adapter = adapter(debug)
    tts_adapter.configure_voice(voice=p_voice_name, language=p_language, speed=p_speed)
    tts_adapter.generate_tts(p_text)
    tts_adapter.save_tts(p_filename)
    tts_adapter.finish()