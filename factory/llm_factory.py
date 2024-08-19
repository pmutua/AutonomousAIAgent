import logging
from llms.llm_interface import LLMInterface
from llms.openai_llm import OpenAI_LLM
from llms.claude_llm import Claude_LLM
from llms.custom_llm import CustomLLM
from config.settings import Settings

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class LLMFactory:
    """
    A factory class to create instances of different LLMs based on the configuration.
    """
    
    @staticmethod
    def get_llm(provider: str, api_key: str = None) -> LLMInterface:
        """
        Create an instance of the specified LLM based on the provider.

        Parameters
        ----------
        provider : str
            The provider of the LLM ("openai", "claude", or "huggingface").
        api_key : str, optional
            The API key to use for authenticating with the LLM. If not provided, will use the key from settings.

        Returns
        -------
        LLMInterface
            An instance of the LLMInterface for the specified provider.
        """
        if provider == 'openai':
            if not api_key:
                raise ValueError("API key must be provided for OpenAI.")
            logging.info("Creating OpenAI LLM with API key: %s...", api_key[:5])
            return OpenAI_LLM(api_key)
        
        elif provider == 'anthropic':
            if not api_key:
                raise ValueError("API key must be provided for Anthropic.")
            logging.info("Creating Claude LLM with API key: %s...", api_key[:5])
            return Claude_LLM(api_key)
        
        elif provider == 'huggingface':
            if not api_key:
                raise ValueError("API key must be provided for Hugging Face.")
            logging.info("Creating Hugging Face LLM with API key: %s...", api_key[:5])
            return CustomLLM(
                repo=Settings.DEFAULT_HUGGINGFACE_REPO,
                prompt_template="You are a helpful assistant. Answer the following question: {question}"
            )
        
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")
