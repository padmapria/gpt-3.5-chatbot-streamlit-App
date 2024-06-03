# Chat-w-CSV-Streamlit-App
An LLM-powered Streamlit app to chat with GPT.

## How to Run the App
**Note:** OpenAI immediately revokes the API key once it detects that the key has been exposed publicly. Therefore, do not expose your API key.

Generate your OpenAI API key here: [Click Here](https://platform.openai.com/account/api-keys)

### Run Locally
To keep the key private, store it in an environment variable named 'OPENAI_API_KEY' in your OS:   

1. Create a `.env` file and store the key as follows:     
OPENAI_API_KEY='YOUR_API_KEY_HERE'

2. Refer to the key in `app.py` by:
```python
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
```

3. Ensure Streamlit is installed on your system and run the app using the below commands from command prompt:

git clone https://github.com/padmapria/gpt-3.5-streamlit-chatbot.git    
cd gpt-3.5-streamlit-chatbot  	  
pip install -r requirements.txt    
streamlit run main.py    

4. Run on Streamlit Cloud   
To deploy the app on Streamlit Cloud:     

i) Do not use a .env file. Instead, set the OPENAI_API_KEY as a secret in the Streamlit Cloud dashboard under your app settings.   
ii) Ensure the rest of your application is set up to pull the API key from the environment variables.    
iii) Follow the instructions on Streamlit Cloud to deploy your app.    

This approach avoids exposing your API key and utilizes Streamlit's built-in secret management.   


