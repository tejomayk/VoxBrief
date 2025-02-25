# Internet Accessibility Assistant
### Making the internet accessible to everyone
An AI-powered tool that converts webpage content into concise voice summaries, making the internet more accessible for visually impaired users and multitaskers.

### Features
- Extracts readable text from any webpage
- Summarizes long content using AI
- Converts summaries into natural voice audio
- Works via a simple Chrome extension

### Proposed Tech Stack
- Backend: FastAPI, Python, Transformers (BART)
- Web Scraping: BeautifulSoup
- Text-to-Speech: Google TTS (gTTS)
- Frontend: JavaScript (Chrome Extension)

### How It Works (Preview)
1. The Chrome extension sends the current webpage URL to the FastAPI backend.
2. The backend extracts and cleans the text using web scraping.
3. The text is summarized using an AI model.
4. The summary is converted into speech using text-to-speech technology.
5. The user receives both the text summary and an audio file for playback.


### Future Improvements (Not planned in this version)
- Support for multiple languages
- Real-time voice interaction
- PDF and document summarization

### License
This project is open-source and available under the MIT License.