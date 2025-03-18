
# Trust Builder Chatbot

This is an AI-powered chatbot that helps users set up private trusts. It uses OpenAI's GPT-4 model and a Flask API to interact with users and provide structured guidance on trust creation.

## Features
- Guides users through private trust setup
- Asks structured questions to gather necessary details
- Provides legal insights (but does not replace legal advice)
- Can be integrated into a website for user interaction

## Installation

### Prerequisites
Make sure you have **Python 3.7+** installed on your system.

### 1. Clone the Repository
If using GitHub, run the following command:
```bash
git clone https://github.com/your-repo/trust-builder-chatbot.git
cd trust-builder-chatbot
```

### 2. Install Dependencies
Run the following command to install required Python libraries:
```bash
pip install openai flask gunicorn
```

### 3. Set Your OpenAI API Key
Edit `app.py` and replace `your-api-key-here` with your actual OpenAI API key:
```python
OPENAI_API_KEY = "your-api-key-here"
```

### 4. Run the Chatbot Locally
Start the chatbot with:
```bash
python app.py
```
This will launch the chatbot on `http://127.0.0.1:5000`

## Deploying to Render
1. Create an account at [Render.com](https://render.com/).
2. Create a new **Web Service**.
3. Connect your GitHub repository.
4. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
5. Deploy the service.
6. Render will provide a public URL (e.g., `https://your-chatbot.onrender.com`).

## API Usage
Once deployed, you can send a **POST request** to:
```bash
https://your-chatbot.onrender.com/chat
```
With JSON data:
```json
{
  "message": "What is a private trust?"
}
```
The chatbot will respond with structured guidance.

## Integration with Website
To embed this chatbot in a website, use JavaScript to send user messages to the API and display responses dynamically.

## Disclaimer
This chatbot provides general information about trusts but **is not a substitute for professional legal advice**. Always consult an attorney for specific legal guidance.

## License
This project is open-source under the MIT License.
