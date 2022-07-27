# EZTTS

Easy Text To Speech is a Python package designed to make TTS in Python easy. It includes a simple interface to multiple different TTS APIs, and a modular framework for adding new TTS engines.

Support for different languages, voices, speeds, etc. are dependent upon the individual adapters.


## Supported Languages, Voices, etc.

As previously mentioned, support for languages, voices, etc. comes from the individual adapters.

There are currently two adapters:

### FTTSAdapter

FTTSAdapter is an adapter that takes from the hidden API at [fromtexttospeech.com](http://http://www.fromtexttospeech.com/). The API was found using web page debug tools. I'm not sure what backend the site uses for TTS generation. Supported voices, languages, and speeds can be found at the [FTTSAdapter README](./eztts/adapters/ftts/README.md).

### GTTSAdapter

GTTSAdapter is an adapter that uses Google's TTS API via the [gTTS library](https://pypi.org/project/gTTS/). More info can be found at the [GTTSAdapter README](./eztts/adapters/gtts/README.md).


## Installation

Currently, this package is not on PyPI. However, it is available here on github, and can be installed with pip:

```
pip install git+https://github.com/trevin-j/eztts.git
```

This will automatically install this package, along with all its dependencies, even optional ones.

### Installing optional dependencies

Some adapters for this package cannot be used unless certain optional dependencies are installed. To install these dependencies, run the following command:

```
py -m eztts --install-optional-dependencies
```

Continue to enter the numbers of the dependencies you want to install, comma separated.

## Usage

It is very simple and easy to use this package. The package supports importing into a Python module, or running in the command line.

### Command Line Usage

Use the command line to generate TTS. Invoke the program by running either `py -m eztts` (Windows), or `python3 -m eztts` (Linux/Mac), or even by simply `eztts`. The program requires arguments to process TTS. The most basic of a command is:

```
eztts -t "Hello, world!" -f "hello.mp3"
```

Run `eztts --help` for more information.


### Python Module Usage

There are two ways to use this as a module. One way is more verbose, and the other way requires only a single line of code, and that single function does the first way under the hood, as well as take care of a bunch of stuff automatically for us. The first way involves importing the specific adapter that you want to use:

```Python
from eztts.adapters.ftts import FTTSAdapter
```

From here, the steps are:
1. Initialize
2. Configure
3. Generate
4. Save
5. Finish

In the code, it looks like this:

```Python
tts_adapter = FTTSAdapter(debug=True)
tts_adapter.configure_voice(voice="Harry", speed="fast")
tts_adapter.generate_tts("Hello, I'm Harry.")
tts_adapter.save_tts("hello.mp3")
tts_adapter.finish()
```

Usually, if you know what voice you want to use, the language will be inferred, unless there are two different language voices with the same name. In that case, you will want to specify the language, or it will default to the first language that matches the voice name. Speed is independent of language and voice, but will depend on the adapter. Selecting a language and not voice will result in the default voice for that language being used.

If you have an adapter you want to use, you can check what languages, voices, and speeds it supports.

```Python
adapter = FTTSAdapter()
print("Supported languages:")
print(adapter.get_supported_languages())

print("Supported English US voices:")
print(adapter.get_supported_voices_by_language("US English"))

print("Supported speeds:")
print(adapter.get_supported_speeds())
```

Notice how we specified US English, and not just English. Each adapter is meant to support a language without specifying the locale, but if the adapter supports multiple locales for the same language, not specifying the locale will result in the adapter picking the default locale, not every locale for that language.

If we want to use the second, easier way, we can simply import and use the tts function.

```Python
from eztts import tts

tts(
    text="Hello, world!",
    filename="hello.mp3",
    voice="Harry",
    speed="medium"
)
```

This function will infer language and adapter based on voice. You can also choose to specify either one, or both. Picking incompatible combinations will result in an error, however. In order to specify an adapter, you must import it and pass the *class* (not an instance of the class) as the specified_adapter parameter.

Chack out each individual adapter's README files for information about voce, language, and speed options, as well as pros and cons for each adapter.

To learn how to implement an adapter, see the [adapters README](./eztts/adapters/README.md).

## NOTES:

1. This project is in no way affiliated with Google, or any other company or organization which provides TTS services through APIs. These APIs may not even be official, and upstream changes may happen without notice and break adapters for this project.

2. Many TTS configurations are not fully tested, and there may be issues with some voice configurations.
