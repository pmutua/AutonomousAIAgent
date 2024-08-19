from config.settings import Settings
from factory.llm_factory import LLMFactory

def print_environment_settings():
    """Print all relevant environment settings for the application."""
    print("Application Name:", Settings.APP_NAME)
    print("Debug Mode:", Settings.DEBUG)
    print("Log Level:", Settings.LOG_LEVEL)
    print("Database URL:", Settings.DATABASE_URL)
    print("Timezone:", Settings.TIMEZONE)
    print("OpenAI API Key:", Settings.OPENAI_API_KEY)
    print("Claude API Key:", Settings.CLAUDE_API_KEY)
    print("Hugging Face API Key:", Settings.HUGGINGFACE_API_KEY)
    print("LLM Provider:", Settings.LLM_PROVIDER)

def main():
    # Load LLM provider and API key from configuration
    llm_provider = Settings.LLM_PROVIDER
    api_key = Settings.get_api_key(llm_provider)

    # Create LLM instance using the factory
    llm = LLMFactory.get_llm(llm_provider, api_key)
    # print(llm)
    # Generate response from LLM
    # response = llm.generate_response("What is the weather like today?")
    
    # Print the response
    # print(response)

if __name__ == "__main__":
    main()
    # print_environment_settings()
