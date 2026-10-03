# hello.py
# Import the official Ollama Python client.
# It talks to the Ollama app already running on your Mac.
import ollama

# chat() sends one user message to a local model and waits for the reply.
# model= must match a model you already pulled (ollama pull llama3.2).
response = ollama.chat(
    model="llama3.2",
    messages=[
        # role "user" means this text is the human prompt.
        {"role": "user", "content": "Say hi in 5 words."}
    ],
)

# The reply is a dict. The text lives at response["message"]["content"].
print(response["message"]["content"])