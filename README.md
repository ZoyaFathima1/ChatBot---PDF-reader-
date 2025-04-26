<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>PDF Question-Answering Chatbot</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f8f9fa;
      color: #212529;
      margin: 0;
      padding: 2rem;
      line-height: 1.6;
    }

    h1, h2 {
      color: #2c3e50;
    }

    h1 {
      margin-bottom: 0.5rem;
    }

    .features, .tech-stack, .installation {
      background-color: #ffffff;
      padding: 1.5rem;
      border-radius: 12px;
      margin-bottom: 1.5rem;
      box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    code, pre {
      background-color: #eef1f4;
      padding: 0.5rem;
      border-radius: 5px;
      display: block;
      overflow-x: auto;
    }

    img {
      width: 100%;
      max-width: 600px;
      border-radius: 8px;
      margin: 1rem 0;
    }

    a {
      color: #007BFF;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    ul {
      padding-left: 1.5rem;
    }
  </style>
</head>
<body>

  <h1>📚 PDF Question-Answering Chatbot using Gemini API</h1>
  <p>A smart, AI-powered chatbot that enables users to upload any PDF file and ask context-aware questions related to the content. Built with Python, Streamlit, and Gemini API, this chatbot reads and understands complex documents, making it a powerful tool for document analysis and assistance.</p>

  <div class="features">
    <h2>🚀 Features</h2>
    <ul>
      <li>📄 Upload any PDF file</li>
      <li>🤖 Ask questions based on the PDF content</li>
      <li>🔍 Gemini-powered contextual understanding and intelligent answers</li>
      <li>⚡ Fast and interactive user interface using Streamlit</li>
      <li>💬 Chat-based UI for a seamless Q&A experience</li>
    </ul>
  </div>

  <div class="tech-stack">
    <h2>🛠️ Tech Stack</h2>
    <ul>
      <li><strong>Frontend & Deployment:</strong> Streamlit</li>
      <li><strong>Backend & Logic:</strong> Python</li>
      <li><strong>PDF Parsing:</strong> PyMuPDF / pdfplumber</li>
      <li><strong>NLP Engine:</strong> Google Gemini API</li>
      <li><strong>Optional:</strong> FAISS / Chroma / Pinecone for vector DB support</li>
    </ul>
  </div>

  <div class="screenshot">
    <h2>📸 Screenshot</h2>
    <img src="1.png" alt="PDF Chatbot Screenshot" />
    <img src="2.png" alt="PDF Chatbot Screenshot" />
    <!-- Replace "screenshot.png" with your actual file name -->
  </div>

  <div class="installation">
    <h2>📦 Installation & Usage</h2>
    <pre><code># Clone the repository
git clone https://github.com/my-username/pdf-gemini-chatbot.git
cd pdf-gemini-chatbot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py</code></pre>
  </div>

  <h2>🔐 API Key Setup</h2>
  <pre><code># In a .env file:
GEMINI_API_KEY=your_key_here</code></pre>

 

</body>
</html>

