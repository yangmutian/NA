"""
Configuration settings for the material analysis framework.
"""

# API settings
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL_NAME = "gpt-4o-mini-2024-07-18"
DEFAULT_TEMPERATURE = 0.3

# Paths
DEFAULT_LOG_FILE = "material_analysis.log"

# LLM Agent configuration
AGENT_TYPE = "CONVERSATIONAL_REACT_DESCRIPTION"
MEMORY_KEY = "chat_history"

# Get API key from environment or use default

# Training configuration
TRAINING_CONFIG = {
    'DATA_PATH': './data/train.csv',
    'MODEL_OUTPUT_PATH': './model/catboost_model.cbm',
    'TEST_SIZE': 0.2,
    'RANDOM_STATE': 42,
    'VERBOSE': 100,
    'MODEL_PARAMS': {
        'iterations': 1000,
        'learning_rate': 0.05,
        'depth': 6,
        'loss_function': 'Logloss'
    }
} 