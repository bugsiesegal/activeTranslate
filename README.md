# Active Translate 🎧🗣️

## Project Overview
Active Translate is a real-time conversation translation system designed for mobile use. The application aims to enable seamless multilingual conversations by providing instant audio translation through headphones.

## Architecture
The system uses a client-server architecture:
- **Server**: Handles speech recognition and translation processing
- **Client**: Mobile interface for audio input/output, built with Kivy

## Features
- Real-time speech recognition
- Text-to-speech translation output
- Mobile-friendly interface
- Network-based client-server communication

## Technical Stack
- **Frontend**: Kivy (Python UI framework)
- **Speech Recognition**: `speech_recognition` library
- **Translation**: `deep_translator`
- **Text-to-Speech**: `pyttsx3`
- **Network**: Python socket communication

## Setup and Installation

### Server Setup
1. Install required dependencies:
```bash
pip install speech_recognition deep_translator pyttsx3
```
2. Run the server:
```bash
python host.py
```

### Client Setup
1. Install additional dependencies:
```bash
pip install kivy
```
2. Navigate to the Client folder and run:
```bash
python client.py
```

## Usage
1. Start the server on your computer/server
2. Connect the client using the server's IP address and port
3. Put on headphones
4. Start speaking - the app will:
   - Capture speech
   - Send it to the server
   - Receive translation
   - Play translated audio through headphones

## Current Limitations
- Latency issues affect real-time performance
- iOS deployment requires additional configuration
- Server and client need to be on the same network
- Network speed significantly impacts user experience

## Future Improvements
- Reduce translation latency
- Implement local processing for offline use
- Add iOS-specific optimizations
- Include multiple language support
- Improve audio quality
- Add background noise reduction

## Project Structure
```
ActiveTranslate/
├── host.py           # Server implementation
└── Client/
    └── client.py     # Kivy-based mobile client
```

## Technical Implementation Details
- Uses WebSocket communication for real-time data transfer
- Implements threading for concurrent audio processing
- Handles audio streaming and buffering
- Manages network connection state

## Contributing
Please just don't try. Why would you?

---
*Created as a vacation project to enable real-time conversation translation*
