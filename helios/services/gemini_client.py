from google import genai
from google.genai import types

from helios.config import GEMINI_API_KEY

MODEL_NAME = "gemini-2.5-flash"

_client = None

def get_client():
    global _client
    if _client is None:
        if not GEMINI_API_KEY:
            raise ValueError("No API key was provided. Please pass a valid API key.")
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client

def generate(
    prompt,
    is_json=False,
    temperature=0.2,
    max_tokens=2048
):
    """
    Central Gemini interface.

    Parameters
    ----------
    prompt : str
    is_json : bool
    temperature : float
    max_tokens : int

    Returns
    -------
    str
    """
    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_tokens
    )
    if is_json:
        config.response_mime_type = "application/json"

    try:
        client = get_client()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config
        )

        return response.text

    except Exception as e:
        raise RuntimeError(
            f"Gemini generation failed: {e}"
        )

