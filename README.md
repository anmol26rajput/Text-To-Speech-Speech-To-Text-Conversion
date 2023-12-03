# Text-to-Speech and Speech-to-Text Conversion Application

This Python application is designed to convert text into speech and speech into text using libraries such as `gTTS` (Google Text-to-Speech) and `SpeechRecognition`.

## Features

- **Text-to-Speech Conversion:** Converts written text into spoken words.
- **Speech-to-Text Conversion:** Transcribes spoken words into written text.
- **Language Support:** Supports multiple languages for both input and output.

## Requirements

- Python 3.x
- Required libraries can be installed via `pip`:
  ```bash
  pip install gTTS SpeechRecognition
  ```

## Usage

### Text-to-Speech Conversion

Run `text_to_speech.py` and follow the instructions:

1. Enter the text you want to convert into speech.
2. Choose the language for the speech output.
3. The application will generate an audio file with the converted speech.

### Speech-to-Text Conversion

Run `speech_to_text.py` and follow the instructions:

1. Speak clearly into the microphone.
2. The application will transcribe your speech into text.
3. The text output will be displayed on the console.

## Files

- `text_to_speech.py`: Contains the code for text-to-speech conversion.
- `speech_to_text.py`: Contains the code for speech-to-text conversion.
- `audio_files/`: Directory where generated audio files are stored (for text-to-speech conversion).

## Usage Example

### Text-to-Speech Conversion

```bash
python text_to_speech.py
```

### Speech-to-Text Conversion

```bash
python speech_to_text.py
```

## Contributors

- Anmol Rajput (https://github.com/anmol26rajput)

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README according to your application's specifics, add troubleshooting instructions, or expand on the usage examples based on your implementation. The provided template offers a basic structure for introducing a Python-based Text-to-Speech and Speech-to-Text conversion application.
