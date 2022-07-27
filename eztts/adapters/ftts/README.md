# FTTSAdapter

The FTTSAdapter is an adapter for EZTTS which provides access to the text-to-speech engine of fromtexttospeech.com. The following is a list of the supported languages, voices, and speeds.

### Supported Languages
* English
* US English
* UK English
* French
* Spanish
* German

### Supported Voices
* English
    * English is an alias for US English, and therefore includes all US English voices.
* US English:
    * Alice
    * Daisy
    * George
    * Jenna
    * John
* UK English:
    * Emma
    * Harry
* French:
    * Jade
    * Gabriel
* Spanish:
    * Isabella
    * Mateo
* German:
    * Michael
    * Nadine

### Supported Speeds
* slow
* medium
* fast
* very fast


## Note

This adapter works by sending a request to the fromtexttospeech.com server to create an mp3 TTS with the specified configuration, and then downloading it. It practically emulates how the server would interact with a user and browser.

This service, while unlimited as far as I have found, is not consistent in how long it takes to generate TTS. It may be nearly instant, or it may take several minutes, if not hours. I believe this is because the server holds a queue of requests, and waits until other requests are finished before yours is accepted. However, due to the inconsistency of how long it takes, this adapter would not be ideal for using with something where fast TTS is important. 

The [GTTSAdapter](../gtts/README.md) provides a more consistently fast TTS engine, and provides more, and different, languages. However, the main benefit to this adapter is its voice variety when compared to gTTS.