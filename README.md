# Streamlit Basics Demo

## Description

This is a beginner-friendly demo app built with **Streamlit** that showcases many of the most commonly used widgets and layout components in the Streamlit library. It's designed as a learning/reference project to understand how different UI elements work — text input, buttons, sliders, dropdowns, file uploads, sidebar, columns, and a basic chat interface.

The app doesn't perform any complex logic — its purpose is purely to demonstrate widget usage and layout patterns that can be reused as building blocks for larger Streamlit projects.

## Features Demonstrated

| Widget/Component | Purpose |
|---|---|
| `st.title()` / `st.header()` | Display page title and section headers |
| `st.text_input()` | Take a single line of text input (name) |
| `st.write()` | Display text/output dynamically |
| `st.button()` | Trigger an action on click |
| `st.number_input()` | Numeric input with min/max/step constraints (age) |
| `st.slider()` | Select a numeric value using a slider (age) |
| `st.selectbox()` | Dropdown selection (course) |
| `st.checkbox()` | Boolean toggle ("I'm not a robot") |
| `st.radio()` | Single-choice selection (gender) |
| `st.text_area()` | Multi-line text input |
| `st.file_uploader()` | Upload files with type restrictions (jpg, raw, zip, jpeg, pdf) |
| `st.sidebar` | Add a sidebar with its own title and dropdown |
| `st.columns()` | Create a two-column layout (input/output side by side) |
| `st.chat_input()` / `st.chat_message()` | Basic chat-style input and message display |

## Prerequisites

- Python 3.8+
- Streamlit library

## Installation

```bash
pip install streamlit
```

## How to Run

1. Save the code in a file, e.g. `app.py`
2. Uncomment the lines you want to run (the code is currently commented out — see note below)
3. Run the app using:

```bash
streamlit run streamlit_code.py
```

4. The app will open automatically in your default browser at `http://localhost:8501`

## Note on the Code

All lines in the provided script are currently commented out (`#`), so running it as-is will produce a blank page. To actually see the widgets render, remove the `#` at the start of each line (or select all and use your editor's "toggle comment" shortcut, e.g. `Ctrl+/` in VS Code).

There's also a small typo to fix before running: `st.chat_message("assistent")` should be `st.chat_message("assistant")` for correct rendering of the assistant's chat bubble icon.

## Project Structure

```
├── app.py          # Main Streamlit application file
└── README.md       # Project documentation (this file)
```

## Possible Next Steps

- Add form validation (e.g., disallow empty name submission)
- Connect the chat input to an actual response-generating function
- Style the app further using `st.set_page_config()` for page title/icon/layout
- Persist user inputs using `st.session_state`
