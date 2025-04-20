import re
from decouple import config

def resolve_env_variables(content: str) -> str:
    """
    Replace placeholders like ${VAR_NAME} in the content string
    with values from the .env file or environment variables.
    """
    return re.sub(r"\$\{(\w+)\}", lambda m: config(m.group(1), default=""), content)