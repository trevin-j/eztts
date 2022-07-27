# GTTSAdapter

This adapter provides access to Google's Text-to-Speech via the gTTS library. When configuring the voice for this adapter, only specify the voice, not the language. This is because each language only supports one voice. Each voice is named "{language} Google". For example, to use US English, specify with "US English Google". You can also just set voice to "Google", which will default to "US English Google".

### Supported Languages
* English
* US English
* UK English
* AU English
* CA English
* IN English
* IE English
* ZA English
* French
* CA French
* FR French
* Mandarin
* Chinese
* CN Mandarin
* TW Mandarin
* Portuguese
* BR Portuguese
* PT Portuguese
* Spanish
* MX Spanish
* ES Spanish
* US Spanish

### Supported Voices
Each language and accent combination has only one available voice.

### Supported Speeds
* slow
* medium