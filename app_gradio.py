# app_gradio.py
import gradio as gr
from qabot import retriever_qa 

# Gradio interface
rag_app = gr.Interface(
    fn=retriever_qa,  
    inputs=[
        gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),
        gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="📄 PDF Q&A Chatbot",
    description="Upload a PDF document and ask any question."
)

if __name__ == "__main__":
    rag_app.launch(server_name="0.0.0.0", server_port=5000)
