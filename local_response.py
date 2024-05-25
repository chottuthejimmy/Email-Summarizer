import requests

def get_local_response(prompt, model=None, stream=False) -> str:
    """
    This function sends a POST request to the local API and returns the response.
    Returns:
        str: The output of the API response, or -1 if the request failed.
             The output JSON file is filtered to return only the value of the response key.
    Future: return other keys as well for evalution of the model
    """

    url = 'http://localhost:11434/api/generate'
    if model is None:
        model = "llama3"
    data = {
    "model": model,
    "prompt":
    f"""
    Summarize the following email content, ensuring the output is in Markdown format. The summary should capture all key points, include any important emojis present in the original message, and preserve important hyperlinks. Follow Markdown syntax for appropriate formatting such as headings, bullet points, and links to make the summary clear and structured.
    Take you time and ensure the summary is concise but comprehensive. Focus on capturing the main ideas and essential information. Avoid including redundant or non-essential details. The goal is to create a summary that provides all necessary information in a brief and clear manner.
    DO NOT TAKE MORE THAN 5 LINES TO SUMMARIZE THE EMAIL.
    Do not include anything like "Here is a summary of the email content in Markdown format:" or "The summary is as follows:".
    Just the direct summary of the email content.
---

{prompt}

---


    """,
    "stream": stream,
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        data = response.json()
        return data['response']  # Only response key is being returned
    else:
        print("Failed to create resource. Status code:", response.status_code)
        return -1

