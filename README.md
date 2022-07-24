# EZTTS

Easy Text To Speech is a simple Python module used to generate speech from text. It has support for multiple voices and will eventually support a few more languages than just English.

I'm not even sure if I'm really supposed to just use fromtexttospeech.com's hidden API, but oh well. Its robots.txt file doesn't really block anything and I couldn't find any restrictions on usage.

## Installation

This isn't currently a package on PyPI, so to use, simply clone the repo and copy the `eztts.py` file, or just directly download the file and put it in your project.

### Dependencies

The following commands can be run to install the dependencies:

```
pip install requests
pip install beautifulsoup4
```

If the module will not work for whatever reason with the above commands, you can download the requirements.txt file and run the following command:

```
pip install -r requirements.txt
```

This will install specific versions of each dependency.

Note: beautifulsoup4 is only used in one single line, so in future versions of this module, it may be removed as a dependency.


## Usage

Using the module is super simple.

### Import the module:

```Python
import eztts
```

### Generating a TTS mp3 file:

Simple way:

```Python
save_tts_mp3("Text to turn to speech", "output.mp3")
```

This will generate speech using the default voice "Alice", which is a US English voice. It also defaults to "medium" speed.

Configurable:

Voice, language, and speed can all be adjusted. Take a look at the docstrings for each class to see what is supported.

If you configure a voice, you only have to specify the language if it is **not** a US English voice. However, you **must** specify it if you are using a non-US English voice.

Using Harry voice, which is a brittish voice, in slow speed, generated to `harry_tts.mp3`:

```Python
text = "But I'm just Harry."
fileout = "harry_tts.mp3"
voice = Voice.EnglishUK.HARRY
language = Language.ENGLISH_UK
speed = Speed.SLOW
save_tts_mp3(text, fileout, voice=voice, language=language, speed=speed)
```

Also, you may print logging info to the console, and save a degub html file by passing "debug=True" to the function.

### Exceptions

I haven't spent enough time working with exceptions, so you'll probably run into them. They will likely be thrown only with network errors of some sort. You'll have to deal with them outside of the function. If you run into a reocurring issue, open an issue on the GitHub repo.
