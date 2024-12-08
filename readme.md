# Fitness Trainer AI

Welcome to **Fitness Trainer AI**, a command-line application designed to provide personalized fitness and nutrition advice through an interactive interface.

## Features

- Interactive Command-Line Interface
- Personalized Workout Plans
- Nutrition Advice

## Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/aayush-ojha/fitness-trainer-ai.git
   cd fitness-trainer-ai
   ```

2. **Set Up a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. **API Keys**

   Create a file named `api_keys.py` in the project root directory and add your Gemini API key:

   ```
   # api_keys.py

   gemini_key = 'your_gemini_api_key_here'
   ```

   > **Note:** Replace `'your_gemini_api_key_here'` with your actual Gemini API key. Keep this file secure and avoid committing it to version control.

## Usage

1. **Activate the Virtual Environment**

   ```
   source .venv/bin/activate
   ```

2. **Run the Application**

   ```
   python3 main.py
   ```

3. **Interact with the Application**

   Follow the on-screen prompts to get fitness advice, workout plans, or nutrition advice.

## Project Structure

```
fitness-trainer-ai/
├── main.py
├── api_keys.py
├── requirements.txt
```

- **main.py:** Main application containing the logic for interacting with the AI.
- **api_keys.py:** Stores your Gemini API key.
- **requirements.txt:** Lists all Python dependencies.

## License

This project is licensed under the MIT License.