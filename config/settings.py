import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

class Settings:
    """
    A class to handle application configuration using environment variables.
    
    Attributes
    ----------
    APP_NAME : str
        The name of the application.
    DEBUG : bool
        Flag to enable or disable debug mode.
    LOG_LEVEL : str
        The logging level for the application.
    DATABASE_URL : str
        The URL for the database connection.
    TIMEZONE : str
        The timezone used in the application.
    OPENAI_API_KEY : str
        API key for OpenAI services.
    CLAUDE_API_KEY : str
        API key for Claude services.
    HUGGINGFACE_API_KEY : str
        API key for Hugging Face services.
    LLM_PROVIDER : str
        The provider of the LLM to use ("openai", "claude", or "huggingface").
    DEFAULT_HUGGINGFACE_REPO : str
        The default repository for Hugging Face models.
    """
    
    # General application settings
    APP_NAME = os.getenv('APP_NAME', 'My Application')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///my_database.db')

    # Other settings
    TIMEZONE = os.getenv('TIMEZONE', 'UTC')

    # API keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY', 'your_claude_api_key_here')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY', 'your_huggingface_api_key_here')

    # LLM settings
    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'anthropic')
    DEFAULT_HUGGINGFACE_REPO = os.getenv('DEFAULT_HUGGINGFACE_REPO', 'mrm8488/t5-base-finetuned-wikiSQL')

    @classmethod
    def get(cls, key, default=None):
        """
        Retrieve a configuration value by its key.
        
        Parameters
        ----------
        key : str
            The key of the configuration value to retrieve.
        default : optional
            The default value to return if the key is not found. Defaults to None.
        
        Returns
        -------
        str or None
            The configuration value associated with the given key, or the default value if the key is not found.
        """
        return getattr(cls, key, default)

    @classmethod
    def get_api_key(cls, provider: str) -> str:
        """
        Retrieve the API key based on the LLM provider.
        
        Parameters
        ----------
        provider : str
            The provider of the LLM ("openai", "claude", or "huggingface").
        
        Returns
        -------
        str
            The API key for the specified provider.
        
        Raises
        ------
        ValueError
            If the provider is not recognized.
        """
        if provider == 'openai':
            return cls.OPENAI_API_KEY
        elif provider == 'anthropic':
            return cls.CLAUDE_API_KEY
        elif provider == 'huggingface':
            return cls.HUGGINGFACE_API_KEY
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")
