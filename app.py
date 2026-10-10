
import os
import gradio as gr
from sources import generate_response


def chatbot_response(message, history):
    if not message or not message.strip():
        return "Please type a message first."

    return generate_response(message.strip(), history)


demo = gr.ChatInterface(
    fn=chatbot_response,
    type="messages",
    title="My AI Chatbot",
    description="Your personal AI assistant powered by Groq.",
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(
        placeholder="Ask me anything...",
        lines=2
    ),
    examples=[
        "Explain machine learning simply.",
        "Help me with mathematics.",
        "Write a Python program to add two numbers."
    ],
    save_history=True
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "7860"))
    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )
