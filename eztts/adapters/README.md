# APIAdapter

The APIAdapter class is an abstract class for implementing a new adapter. It includes a set of methods that provide an easy to use and uniform interface for interacting with the adapter. Implementing a new adapter is simple, and I will go over it here.

## Implementing a New Adapter

### 1: Starting from a template

The first step is to copy the template folder and rename it to the name of your adapter. The template folder is found in the adapters folder.

Inside the folder, there is an \_\_init__.py file. It is filled with template code that you can add to to create a new adapter.

### 2: Adding supported voices, languages, and speeds

Every adapter has to specify what languages, voices, and speeds it supports. Users of the adapter can then use methods implemented in the superclass to get information about what languages, voices, and speeds the adapter supports.

This package encourages using "common names" for naming voices, speeds, and languages. These names are used to specify configurations without the need for checking multiple names. For example, if you have an English voice, one API might handle it as "en", while another might handle it as "ENGLISH". We store supported configurations in a dictionary so that the "common name" can be specified, and converted into the actual name of the voice, language, or speed. In the case of the example, "English" is the common name.

#### Speeds

First, let's cover how to specify speeds, since that is the easiest. The following are the common names for speeds:

* `very slow`
* `slow`
* `medium`
* `fast`
* `very fast`

Fill the `SPEEDS` dictionary with the common names of the supported speeds, and the values adapter-specific names that will be used with the API. For example, the following is how speeds are specified for the FTTSAdapter:

```Python
SPEEDS = {
    "slow": -1,
    "medium": 0,
    "fast": 1,
    "very fast": 2,
}
```

Since FTTS does not support `very slow`, it is not included. For speed, if the user chooses an unsupported speed, the default speed will be used. We will cover defaults later.

gTTS takes a different approach to specifying speeds. Since the way we interact with gTTS speed is through a boolean (`speed=`), gTTS speeds are specified like so:

```Python
SPEEDS = {
    "slow": True,
    "medium": False,
}
```

#### Languages

Now, let's discuss adding supported languages. The common names for languages are structured like "{Language}", where language starts with a capital letter, and the rest are lowercase. If that language has multiple accents supported, accents can be specified as a new entry in the dictionary, formatted as "{2 char accent abbreviation} {Language}", such as "US English". The abbreviation must be capitalized along with the language. To allow searching only by language and not accent, you should always have one version of that language with no accent specified, and it can have the same adapter-specific name as whichever accent you deem "default".


#### Voices

Voices are specified using the following:
`"key": (value1, value2)`,
where `key` is the common name of the voice (whatever you like), `value1` is the common-name of the language that the voice is tied to, and `value2` is the adapter-specific name of the voice.


#### Defaults

To set the defaults, set DEFAULT_SPEED to the common name of the default speed, and DEFAULT_VOICE to the common name of the default voice. There is no default language, since a voice is already tied to a language.


### 3: _setup method

This method is used for any setup that needs to be done before the adapter is used. It is called by the constructor. It can be ommitted if there is nothing to do.

### 4: _take_down method

This method is used for any cleanup that needs to be done after the adapter is used. It is called when the finish method is called. It can be ommitted if there is nothing to do.

### 5: generate_tts method

This method is used to generate TTS. It is called directly on the adapter. In this method, do whatever is necessary to generate the TTS from the passed text. Make sure to save whatever objects will be necessary later, when saving the file, to a new attribute.

Inside this method, you will also need to deal with the voice, language, and speed that were configured. You have easy access to the selected voice, language, and speed, however, there are also different ways to access them based on how you want to use them. As you know if you read above, configurations have a common name and an adapter-specific name. The common names can be accessed by `self._voice`, `self._language`, and `self._speed`. The adapter-specific names can be accessed by `self._adapter_specific_voice`, `self._adapter_specific_language`, and `self._adapter_specific_speed`.

In addition to accessing common and adapter-specific names, you can also access a version that was encoded automatically so that it can be sent in a URL. These can be accessed by `self._encoded_voice`, `self._encoded_language`, and `self._encoded_speed`.

### 6: save_tts method

This method is used to save the TTS. It is called directly on the adapter. In this method, do whatever is necessary to save the TTS to a file with the passed filename.

### 7: Add adapter to program

To use your adapter, it can be added one of two ways.

First, while developing, you can add it to be used by the tts function by appending the the adapter class to the list of valid adapters. This allows adding the adapter without modifying this package's source code. If we created an adapter called `MyTTSAdapter`, we would add it like so:

```Python
from eztts import tts, valid_adapters # We will append our adapter class to the list of valid adapters

from my_tts_adapter import MyTTSAdapter # We will import our adapter class, probably from a local module

# Add our adapter to the list of valid adapters
valid_adapters.append(MyTTSAdapter)

# Generate TTS specifically using our adapter
tts("Hello, world!", "test.mp3", adapter=MyTTSAdapter)
```

Even though we specified the adapter, which means it would override the valid adapters anyways, appending it to the list of valid adapters makes the tts function support searching our adapter and using it if it supports a specified voice.


The second option is to add the adapter to the package. This involves modifying the source of this package, and is recommended if you plan to contribute to, or at least fork, this package.

First, add your adapter folder to the folder of packages. Don't forget to include a readme in your folder to document your adapter!

Now, we need to modify the \_\_init__.py file in the eztts folder. Simply add an import statement and append the class to valid_adapters.

```Python
from .adapters import APIAdapter

valid_adapters = []

from .adapters.ftts import FTTSAdapter
valid_adapters.append(FTTSAdapter)

# Add our new adapter, MyTTSAdapter
from .adapters.my_tts_adapter import MyTTSAdapter
valid_adapters.append(MyTTSAdapter)

...
```

If our new adapter requires any packages that are not required by the base package, these will be considered optional dependencies that are reqiured to use this adapter. So, when we import it and add it, we need to surround with try/except statements in case the dependencies are not installed.

```Python
from .adapters import APIAdapter

valid_adapters = []

from .adapters.ftts import FTTSAdapter
valid_adapters.append(FTTSAdapter)

# Add our new adapter, MyTTSAdapter, which has an optional dependency
try:
    from .adapters.my_tts_adapter import MyTTSAdapter
    valid_adapters.append(MyTTSAdapter)
except ImportError:
    pass

...
```

We also need to include requirements.txt in our adapter's folder so that the optional dependencies are installed if the user chooses. Also, modify the all_adapters file, and add the name of your adapter folder to the list.