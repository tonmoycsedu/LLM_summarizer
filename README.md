# SETUP

This is a simple website with a client and server side. To install:

1. Clone the repo: `git clone https://github.com/tonmoycsedu/LLM_summarizer.git`
2. Go to the folder: `cd LLM_summarizer`


## Server setup
This project contains a python server for contacting the Gemini API.

1. Go to the server folder: `cd server`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:  
    `source venv/bin/activate` (#macOS / Linux) or  
   `venv\Scripts\activate` (# Windows)
5. Install packages: `pip install -r requirements.txt`
6. Get the Gemini API key: got to `https://aistudio.google.com/app/apikey` and create an api key
7. Add API Key in the PATH:  
      `echo 'export GEMINI_API_KEY="your_actual_api_key_here"' >> ~/.zshrc`  
      `source ~/.zshrc`
8. Check API key: `echo $GEMINI_API_KEY`
9. Run the server: `python app.py`. This should start the server in `http://127.0.0.1:5001`

## Client setup
This is Vue.js app. To install, do the following,

1. Open a terminal in the `client` folder.
2. Run `npm install`
3. Run `npm run dev`
4. You should see the follwoing website if you go to: `http://localhost:5173/`



