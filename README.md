# QA Bot with LangChain + LLMs

Welcome to the **QA Bot with LangChain + LLMs** project!  
This repository contains all source code, scripts, and resources for building a document-based question-answering chatbot using LangChain and large language models (LLMs).

---

## 📚 About This Repository

This project allows users to **upload documents** (PDF, TXT, etc.) and **ask questions** in natural language. The bot retrieves relevant context from the uploaded documents and provides **intelligent, context-aware answers** in real-time. It is built with **Python**, **LangChain**, and **Gradio** for an easy-to-use web interface.

### Main Features

- Upload and process documents for Q&A
- Ask questions in natural language
- Real-time, context-aware responses
- Integration with LLMs and LangChain
- Gradio-based web interface

---

## 📁 Repository Structure
```
.
├── app_gradio.py
├── qabot.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```



**Clone the repository:**
```bash
git clone git@github.com:quanho114/pdf-chatbot.git
```

## Run with Python (Local):

**Step 1**
```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

**Step 2**
```
python app_gradio.py
```
Open the URL provided by Gradio in your browser to interact with the QA Bot.

## Run with Docker

**Step 1: Build the Docker image**
```
docker build -t pdf-chatbot .
```
**Step 2: Run the container**
```
Step 2: Run the container
```
- ```-p 7860:7860``` maps the Gradio port inside the container to your host machine.

- After running, open your browser at: ```http://localhost:7860```

**OR Using Docker Compose**
If you have ```docker-compose.yaml``` in the project root:
```
docker compose up --build
```
- This will automatically build the Docker image and run the container.

- Access the app at ```http://localhost:7860```


## 🎬 Demo

Click the link below to view the demo video of the QA Bot in action:

[Watch Demo Video](test/test_01.mp4)

**Example Usage:**  
- Upload a PDF or TXT document  
- Ask: "What is the main topic of this document?"  
- Bot returns a context-aware, intelligent answer instantly

## 🧠 How QA Bot Works

The QA Bot uses **LangChain** and **large language models (LLMs)** to provide context-aware answers from uploaded documents. The workflow is as follows:

1. **Upload Document**: The user uploads a PDF, TXT, or other supported format.  
2. **Document Processing**: The bot reads the content, cleans it, and splits it into manageable chunks.  
3. **Embedding & Vector Store**: Each chunk is converted into embeddings using an LLM, then stored in a vector database for fast similarity search.  
4. **Question Handling**: When the user asks a question, the bot queries the vector store to find the most relevant chunks.  
5. **Answer Generation**: The LLM generates a context-aware response based on the retrieved content.  
6. **Response Display**: The answer is displayed instantly in the **Gradio interface**.

This design allows the bot to answer questions **accurately and in real-time**, even on large documents.

## 🛠️ Requirements / Dependencies

- Python 3.10+
- Gradio
- LangChain
- LLM backend (OpenAI API key or local LLM)
- See `requirements.txt` for full dependency list

## 📖 References

- [LangChain Documentation](https://www.langchain.com/)  
- [OpenAI API Documentation](https://platform.openai.com/docs/)  
- [Gradio Documentation](https://gradio.app/)  
- [IBM AI Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ai-engineer)

## 📝 License

- This project is licensed under the MIT License. See LICENSE for details.
- This repository is intended for educational purposes and personal projects.

## 🙏 Acknowledgements

- Thanks to the developers of LangChain, Gradio, and the open-source AI community for providing excellent tools and resources.
- Special thanks to the contributors and inspirations from QA bot tutorials and document-based LLM applications.


