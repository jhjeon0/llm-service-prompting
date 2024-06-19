import json
from openai import OpenAI


def run(
    system_prompt: str, user_content: str, api_key: str, history=None, json_mode=None
):
    client = OpenAI(api_key=api_key)
    request_param = {
        "messages": [],
        "model": "gpt-3.5-turbo-0125",
        "temperature": 0.35,
        # "model": model,
    }
    if system_prompt is not None:
        request_param["messages"].append(
            {
                "role": "system",
                "content": system_prompt + "\nresponse type is josn\n{'keyword':}",
            }
        )
    if user_content is not None:
        request_param["messages"].append({"role": "user", "content": user_content}),
    if history is not None:
        request_param["messages"] = history

    if json_mode is True:
        request_param["response_format"] = {"type": "json_object"}

    chat_completion = client.chat.completions.create(**request_param)

    if json_mode is True:
        print(json.loads(chat_completion.choices[0].message.content))
        return json.loads(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content
