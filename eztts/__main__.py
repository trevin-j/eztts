from . import tts
import argparse

from .install_dependencies import install_dependencies

def main():
    """
    Entry point for console_scripts
    """
    parser = argparse.ArgumentParser(description="Generate text to speech and save it to a file.")
    parser.add_argument("-t", "--text", help="The text to get TTS from.")
    parser.add_argument("-f", "--filename", help="The output mp3 file. Include '.mp3'")
    parser.add_argument("-v", "--voice", help="The name of the voice to use. Uses default if not passed.")
    parser.add_argument("-s", "--speed", help="The speed to read the text. Uses default if not passed.")
    parser.add_argument("-l", "--language", help="The language of the text. Defaults to English US.")
    parser.add_argument("-q", "--quiet", help="If passed, do not display log messages.", action="store_true")
    parser.add_argument("--install-optional-dependencies", help="If passed, install optional dependencies.", action="store_true")
    parser.add_argument("--branch", help="If passed, install optional dependencies from a specific git branch.", default="master")

    args = parser.parse_args()

    if (args.text and not args.filename) or (not args.text and args.filename):
        print("You must pass both text and filename or neither.")
        return

    if args.text:
            
        # Get the text from the arguments.
        text = args.text

        # Get the filename from the arguments.
        filename = args.filename

        # We want optional arguments to be none if they are not passed.\
        # This allows it to work flawlessly with the default values in the tts function.
        voice_name = args.voice
        speed = args.speed
        language = args.language
        debug = not args.quiet
        
        # Call the tts function.
        tts(
            text=text,
            filename=filename,
            voice_name=voice_name,
            speed=speed,
            language=language,
            debug=debug
        )

    if args.install_optional_dependencies:
        install_dependencies(args.branch)


if __name__ == "__main__":
    main()