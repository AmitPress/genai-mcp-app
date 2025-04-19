# GEN AI VOICE ASSISTANT

In this project, I have demonstrated the use of latest Model Context Protocol or MCP. The goal is to embed context to our AI agent so that it can perform some nice operations and can make a very good automation for our manual tasks.

#### How to run the server

To run the server,...
* Clone this repository
* Copy the contents of `.env.example` to `.env` ( the file is inside the folder call `rag_server` )
* Put your gemini api ( which is free to some extent, if you yet dont have it, nothing blocks you get one from aistudio.google.com ) in `.env` file as the value of `GOOGLE_API_KEY=`

* Now first `cd` into `server` folder and run it `uv run main.py`
* Then `cd` into `rag_server`
* Run initiate `io` pipeline via `python mcp_server.py`
* Now as a last step run the `main.py` with `python main.py` 