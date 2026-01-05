

# 🔗 LinkedIn Post Generator – GenAI Project (Llama 3.2)

## 📌 Project Overview

The **LinkedIn Post Generator** is an end-to-end **Generative AI application** that automatically creates professional LinkedIn posts based on user-selected **topic, language, and length**.
It uses the **Llama 3.2 Large Language Model** with **LangChain** for prompt orchestration and **Streamlit** for an interactive web interface.

This project demonstrates how to build a **real-world GenAI application**, starting from data preprocessing and contextual enrichment to real-time content generation.



<img width="1536" height="1024" alt="ChatGPT Image Jan 4, 2026, 07_43_49 PM" src="https://github.com/user-attachments/assets/f346d08a-1dbe-4856-a34c-b89ea0751a55" />

---

## ✨ Features

* Generate professional LinkedIn posts instantly
* Topic-based content generation (Career, Job Search, Rejection, Motivation, etc.)
* Supports **Short, Medium, and Long** post formats
* Multi-language selection
* Context-aware responses using preprocessed post data
* Clean and responsive Streamlit UI
* Modular and extensible architecture

---

## 🧠 High-Level Architecture


<img width="2752" height="1536" alt="unnamed (3)" src="https://github.com/user-attachments/assets/d620d39d-e8fb-4c6b-95ef-ee5dac6aba71" />


The system is divided into **two main stages**:

### **Stage 1: Data Preparation**

* Raw LinkedIn posts are collected and stored in JSON format
* Posts are cleaned, structured, and enriched
* Metadata such as **topic, language, and length** is added
* Processed posts are stored for contextual grounding

### **Stage 2: Post Generation**

* User selects topic, language, and length from UI
* LangChain builds a structured prompt
* Llama 3.2 generates the LinkedIn post
* Output is displayed in real time in the Streamlit app

---

## 🔄 Data Processing Pipeline

1. Load raw LinkedIn posts from `raw_posts.json`
2. Clean and normalize text data
3. Structure posts with metadata (topic, engagement, etc.)
4. Save enriched posts into `processed_posts.json`
5. Use processed data as contextual examples during generation

This pipeline ensures **better relevance, tone consistency, and output quality**.

---

## 🗂️ Project Structure

```bash
LinkedIn-Post-Generator-Tool-Gen-AI-Project-Using-Llama/
│
├── app.py                     # Main Streamlit application
├── preprocess.py              # Data preprocessing script
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
│
├── data/
│   ├── raw_posts.json         # Raw LinkedIn posts
│   └── processed_posts.json  # Cleaned & enriched posts
│
├── vectorstore/
│   └── chroma_db/             # Vector embeddings storage
│
├── prompts/
│   └── prompt_templates.py   # LangChain prompt templates
│
└── assets/
    └── screenshots/           # Architecture & UI images
```

---

## 🛠️ Technologies Used

### **Programming & Frameworks**

* Python
* Streamlit

### **AI & GenAI**

* Llama 3.2
* LangChain

### **Data & Storage**

* JSON
* ChromaDB (Vector Database)

---

## ⚙️ Core Technologies

* **Streamlit** – Web-based UI for user interaction
* **LangChain** – Prompt engineering and workflow orchestration
* **Vector Database (ChromaDB)** – Context storage and retrieval
* **Llama 3.2** – Large Language Model for text generation

---

## 📚 Key Libraries

* `streamlit` – UI rendering
* `langchain` – Prompt management
* `json` – Data handling
* `chromadb` – Vector storage
* `python-dotenv` (optional) – Environment configuration

---

## 🤖 AI Model

* **Model Name:** Llama 3.2
* **Type:** Large Language Model (LLM)
* **Usage:**

  * Generates professional LinkedIn content
  * Uses contextual examples for better tone and relevance
  * Produces real-time outputs based on structured prompts

---

## 📦 Installation

### 🔧 Prerequisites

* Python **3.8 or higher**
* Git
* Llama 3.2 model access (local or API-based, depending on setup)
* (Optional) Virtual environment tool (`venv` or `conda`)

---

### ⚙️ Setup Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vennelabathini/LinkedIn-Post-Generator-Tool-Gen-AI-Project-Using-Llama.git
cd LinkedIn-Post-Generator-Tool-Gen-AI-Project-Using-Llama
```

---

#### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

* **Windows**

```bash
venv\Scripts\activate
```

* **macOS / Linux**

```bash
source venv/bin/activate
```

---

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#### 4️⃣ Configure Environment Variables (Optional)

If your LLM setup requires API keys or environment configs:

Create a `.env` file in the project root:

```env
LLM_MODEL=llama-3.2
```

> Update variables based on your LLM provider or local setup.

---

#### 5️⃣ Prepare the Data (Optional)

If you want to reprocess LinkedIn post data:

```bash
python preprocess.py
```

This step:

* Loads raw LinkedIn posts
* Cleans and enriches data
* Saves processed posts for generation

---

#### 6️⃣ Run the Application

```bash
streamlit run app.py
```

---

#### 7️⃣ Access the Application

Open your browser and navigate to:

```text
http://localhost:8501
```



## 🧾 Output

* A well-structured, professional LinkedIn post
* Content tailored to user-selected inputs
* Suitable for posting directly on LinkedIn

The output updates **in real time** with each generation.

<img width="1902" height="1033" alt="tool 1" src="https://github.com/user-attachments/assets/aba05999-e7d0-4575-9897-38b52d515317" />



---

## 🔍 How It Works (Step-by-Step)

1. User provides input through Streamlit UI
2. Inputs are passed to LangChain prompt templates
3. Contextual examples are retrieved from processed data
4. Llama 3.2 generates the LinkedIn post
5. The result is displayed on the UI

---

## ⚙️ Configuration

* Update post categories in UI dropdowns
* Modify prompt templates for different writing styles
* Extend data in `raw_posts.json` for better context
* Adjust length rules for short/medium/long posts

---

## 🎯 Use Cases

* Job seekers writing LinkedIn posts
* Career guidance and motivation content
* Influencer and professional branding
* Learning real-world GenAI application development

---


