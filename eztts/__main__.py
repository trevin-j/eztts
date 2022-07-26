from . import tts
import argparse

def main():
    """
    Entry point for console_scripts
    """
    parser = argparse.ArgumentParser(description="Generate text to speech and save it to a file.")
    parser.add_argument("-t", "--text", help="The text to get TTS from.", required=True)
    parser.add_argument("-f", "--filename", help="The output mp3 file. Include '.mp3'", required=True)
    parser.add_argument("-v", "--voice", help="The name of the voice to use. Uses default if not passed.")
    parser.add_argument("-s", "--speed", help="The speed to read the text. Uses default if not passed.")
    parser.add_argument("-l", "--language", help="The language of the text. Defaults to English US.")
    parser.add_argument("-d", "--debug", help="If passed, do display debug messages.", action="store_true")

    args = parser.parse_args()

    # Get the text from the arguments.
    text = args.text

    # Get the filename from the arguments.
    filename = args.filename

    # We want optional arguments to be none if they are not passed.\
    # This allows it to work flawlessly with the default values in the tts function.
    voice_name = args.voice
    speed = args.speed
    language = args.language
    debug = args.debug
    
    # Call the tts function.
    tts(
        text=text,
        filename=filename,
        voice_name=voice_name,
        speed=speed,
        language=language,
        debug=debug
    )