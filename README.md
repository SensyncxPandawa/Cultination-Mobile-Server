## Development Setup Requirements

- Python 3.7 or later
- Windows, MacOS, and Linux development environments are supported

## Development Setup Instructions

Assuming the development setup requirements above have been satisfied,
run the following in a terminal (git-bash is recommended on Windows) after cloning the repo
to set up your local development environment.

```bash
# Install local dev requirements, ideally in an isolated Python 3.7 (or later) environment
pip install -r requirements.txt
```

## Running the Development Server

The local dev server runs via uvicorn...

```bash
# Cross-platform, works on Windows, MacOS and Linux
uvicorn app.main:application --reload

# Alternate method of running local dev server via npm
npm start
```
