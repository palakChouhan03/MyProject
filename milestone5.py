import requests

def query_llm(prompt):
    api_key = "YOUR_LLM_API_KEY"
    response = requests.post(
        "LLM_ENDPOINT_URL",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"prompt": prompt}
    )
    return response.json()["reply"]

@app.post("/chat/")
def chat(prompt: str):
    llm_response = query_llm(prompt)
    return {"response": llm_response}