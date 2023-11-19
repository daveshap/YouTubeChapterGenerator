# YouTubeChapterGenerator

## Overview
YouTubeChapterGenerator is a tool designed to automate the creation of YouTube chapter markers from video transcripts. It utilizes various Python scripts to clarify, concatenate, and convert transcripts, leveraging OpenAI's GPT-3 for text processing.

## Key Components

### 1. clarify_transcripts.py
This script clarifies YouTube video transcripts using OpenAI's GPT-3 API. It reads transcripts, sends them to GPT-3 for clarification, and saves the processed transcripts.

### 2. concatenate files.py
Concatenates individual transcript files into a single output file for ease of processing. It adds markers to distinguish between different videos in the output.

### 3. convert_transcript_to_spr.py
Converts transcript files into a specific format suitable for speech recognition or further processing. This script reads each transcript, processes it using a chatbot function powered by GPT-3, and saves the output in a new format.

## Usage
- Ensure you have Python installed.
- Install required dependencies: `pip install -r requirements.txt` (if a requirements file exists).
- Run each script as needed:
  - `python clarify_transcripts.py` for transcript clarification.
  - `python concatenate files.py` for concatenating transcripts.
  - `python convert_transcript_to_spr.py` for converting transcripts.

## Contributions
Contributions are welcome. Please open an issue or submit a pull request for any enhancements.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or assistance, please open an issue in this repository.
