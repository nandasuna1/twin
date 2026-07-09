# Digital Twin 🧑‍💻

This is my **AI Digital Twin** — a chatbot built to represent me and talk about my
professional career, background, skills, and experience, just like I would.

I built this project as a hands-on way to **learn about AI agents**: how they're
structured, how they use tools, and how to give them context and personality so
they can hold a real conversation on someone's behalf.

## What it does

The twin is a chat interface where visitors can ask questions about my career.
It answers in character, using my LinkedIn profile and a personal summary as
context. If it doesn't know the answer, or a visitor wants to get in touch, it
uses tools to record that information so I can follow up later.

## How it works

- **`app.py`** — Entry point. Runs a [Gradio](https://www.gradio.app/) chat UI
  and drives the conversation loop with the LLM, handling tool calls until a
  final response is ready.
- **`context.py`** — Builds the system prompt, loading my LinkedIn profile
  (`Profile.pdf`) and a short personal summary (`summary.txt`) into the twin's
  context so it can answer questions accurately.
- **`tools.py`** — Defines the tools the agent can call:
  - `record_user_details`: saves a visitor's contact info when they want to
    get in touch.
  - `record_unknown_question`: logs any question the twin couldn't answer,
    so it's never left making things up.
  
  Notifications for both are sent via [Pushover](https://pushover.net/).
- **`styles.py`** — Custom CSS/JS and example prompts for the chat UI.

The model is served through an OpenAI-compatible endpoint pointing at
Google's Gemini API (`gemini-2.5-flash-lite`).

## Running it locally

1. Install dependencies (this project uses [uv](https://github.com/astral-sh/uv)):
   ```bash
   uv sync
   ```
2. Create a `.env` file with the required environment variables:
   ```
   GEMINI_API_KEY=your_key_here
   PUSHOVER_USER=your_pushover_user_key
   PUSHOVER_TOKEN=your_pushover_app_token
   ```
3. Run the app:
   ```bash
   uv run app.py
   ```
4. Open the local Gradio URL printed in the terminal and start chatting.

## Why I built this

I wanted to get practical experience with the core building blocks of AI
agents — system prompts, grounding an LLM with personal context, and tool
calling — by building something small, personal, and genuinely useful: a
digital version of me that can talk about my career when I'm not around to
do it myself.
