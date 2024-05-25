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
    {prompt}
    Summarize this in a couple of sentences, keep it short and sweet.
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

