# AutonomousAIAgent

## Overview

This application provides an interface for interacting with different Language Models (LLMs) like OpenAI and Claude. It allows you to configure and generate responses from these models using a factory pattern.

## Features

- Support for multiple LLMs (OpenAI, Claude)
- Configuration via environment variables
- Mocking and testing support

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` for installing Python packages

### Setup

1. **Clone the Repository**
   <br>
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

   ```

2. **Create and Activate a Virtual Environment**
    <br>
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

    ```

3. **Install Dependencies**
    <br>
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env File**

    Copy the example .env file and update it with your API keys and other configuration settings:

    ```bash
    cp .env.example .env

    ```

    Edit `.env` to include your configuration:
    <br>
    ```env
    APP_NAME=My Application
    DEBUG=True
    LOG_LEVEL=DEBUG
    DATABASE_URL=sqlite:///my_database.db
    TIMEZONE=UTC
    OPENAI_API_KEY=your_openai_api_key_here
    CLAUDE_API_KEY=your_claude_api_key_here
    ```

## Usage

### Running the Application

To run the main script, execute:

```bash
python main.py
```

## Configuration

Configuration is handled via the .env file. You can set the following environment variables:

- APP_NAME: Application name
- DEBUG: Debug mode (True/False)
- LOG_LEVEL: Logging level
- DATABASE_URL: Database connection URL
- TIMEZONE: Timezone for the application
- OPENAI_API_KEY: API key for OpenAI
- CLAUDE_API_KEY: API key for Claude

## API Keys

Ensure you have valid API keys for the LLMs you intend to use and update them in the `.env` file.

## Testing

### Running Tests

To run the tests, use the following command:

With `unittest`:

```bash
python -m unittest discover -s tests
```

With pytest:

```bash
pytest
```

## Development

### Adding New Features

1. Create a new branch for your feature:

```bash
git checkout -b feature/your-feature
```

2. Implement your changes and add tests as needed.

3. Commit your changes:

    ```bash
    git add .
    git commit -m "Add feature: your feature description"
    ```

4. Push your branch and create a pull request.

## Code Style

Follow PEP 8 guidelines for Python code style.

## Documentation

- Ensure your code is well-documented with docstrings.
- Update this README file with relevant changes.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow for issues and pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or issues, please contact `pmutua [at] live [dot] com`.

Feel free to replace placeholders such as repository URLs, API keys, and contact information with your specific details.
