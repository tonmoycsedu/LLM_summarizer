# SETUP

This is a simple website with a client and server side. To install:

1. Clone the repo: `git clone https://github.com/tonmoycsedu/LLM_summarizer.git`
2. Go to the folder: `cd LLM_summarizer`


## Server setup
This project contains a python server for contacting the Gemini API.

1. Go to the server folder: `cd server`
2. Remove the venv folder under the server folder.
3. Follow either step 3 or step 4.  
   a. create a virtual environment: `python -m venv venv`.  
   b. Activate the virtual environment:     
      `source venv/bin/activate` (#macOS / Linux) or  
      `venv\Scripts\activate` (# Windows)  
   c. Install packages: `pip install -r requirements.txt`
7. install google genai and flask python packages: `pip install -q -U google-genai flask flask-cors`
8. Get the Gemini API key: got to `https://aistudio.google.com/app/apikey` and create an api key.  
9. Add API Key in the PATH:  
   For MacOS:    
      `echo 'export GEMINI_API_KEY="your_actual_api_key_here"' >> ~/.zshrc`  
      `source ~/.zshrc`    
   For Windows in Powershell:  
       `[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "your_actual_api_key_here", "User")`
10. Check API key:  
    For MacOS: `echo $GEMINI_API_KEY`  
    For Windows: `echo $env:GEMINI_API_KEY`
12. Run the server: `python app.py`. This should start the server in `http://127.0.0.1:5001`

## Client setup
This is Vue.js app. To install, do the following,

1. Open a terminal in the `client` folder.
2. Run `npm install`
3. Run `npm run dev`
4. You should see the follwoing website if you go to: `http://localhost:5173/`

<img width="1434" height="529" alt="Screenshot 2025-10-08 at 12 49 19 AM" src="https://github.com/user-attachments/assets/4c42d0de-fc9e-42ce-ad09-934c323f1be1" />
