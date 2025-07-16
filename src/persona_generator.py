from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def generate_persona_with_mistral(user_content: str, api_key: str) -> str:
    client = MistralClient(api_key=api_key)

    prompt = f"""
    Analyze the following Reddit content and generate a detailed user persona.
    Include: Age, Occupation, Personality Traits, Motivations, Goals, Frustrations.
    Also cite specific quotes used from the content for each point.

    Content:
    {user_content}
    """

    messages = [ChatMessage(role="user", content=prompt)]
    response = client.chat(model="mistral-medium", messages=messages)
    return response.choices[0].message.content
