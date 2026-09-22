MASTER_PROMPT = """
You are a professional enterprise customer service assistant.
Only answer using the context provided.

Context: {context}

User Query: {user_query}
"""

def compile_prompt(context, query):
    return MASTER_PROMPT.format(context=context, user_query=query)

print(compile_prompt("The Customer's order was shipped yesterday.", "When was my order shipped?"))

def mock_api_response():
    return {
        "content": [
            {
                "text": "Your processed output token text here"
            }
        ],
        "usage": {
            "input_tokens": 45,
            "output_tokens": 120
        }
    }

response = mock_api_response()

raw_text = response.get("content", [{}])[0].get("text", "No text available")

print("Raw Text:", raw_text)

usage = response.get("usage", {})

input_tokens = usage.get("input_tokens", 0)
output_tokens = usage.get("output_tokens", 0)

total_tokens = input_tokens + output_tokens

print("Input Tokens:", input_tokens)
print("Output Tokens:", output_tokens)
print("Total Tokens:", total_tokens)