Here's your **updated GitHub README** with **Streamlit** included for app deployment:  

---

# **🚀 AI-Powered Cold Email Generation**  

## **📌 Overview**  
This project automates the process of generating **B2B cold emails** using **LLMs, vector databases, and Streamlit** for a user-friendly interface.  

Companies often hire professionals from other firms for projects. To facilitate this, organizations send **cold emails** by extracting job postings from official websites. This project uses **LangChain, ChromaDB, and ChatGroq LLM** to streamline and automate the process, generating **personalized cold emails** based on extracted job descriptions.  

---

## **🔹 Project Workflow**  

### **1️⃣ Extract Job Postings**  
- Scrape career pages using **LangChain’s WebBaseLoader**.  

### **2️⃣ Process with LLM**  
- Pass extracted job descriptions to an **LLM** (ChatGroq).  
- Generate a structured **JSON** containing:  
  - Job Role  
  - Required Skills  
  - Additional Metadata  

### **3️⃣ Store in ChromaDB**  
- Store job roles and required skills in **ChromaDB** for efficient retrieval.  

### **4️⃣ Generate Cold Email**  
- Retrieve relevant job postings from **ChromaDB**.  
- Use **Prompt Engineering & Chaining** to generate a **personalized cold email**.  

### **5️⃣ Deploy with Streamlit**  
- Build a **user-friendly web app** using **Streamlit**.  
- Users can enter a job role, and the app generates a **cold email** dynamically.  

---

## **🔹 Code Implementation**  

### **1️⃣ Extract Job Data**
```python
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com/careers")
content = loader.load()
```

### **2️⃣ LLM Processing (Job Role & Skills Extraction)**
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Extract job roles and skills from: {page_data}")
chain_extract = prompt_template | llm  
result = chain_extract.invoke({"page_data": content})
```

### **3️⃣ Store in ChromaDB**
```python
import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("job_roles")

collection.add(
    documents=[result["job_role"]],
    metadatas=[{"skills": result["skills"]}],
    ids=["job_123"]
)
```

### **4️⃣ Retrieve & Generate Cold Email**
```python
links = collection.query(query_texts=result["skills"], n_results=2).get('metadatas', [])
prompt_email = PromptTemplate.from_template("Generate a cold email for: {job_description} with references {link_list}")

chain_email = prompt_email | llm  
email_result = chain_email.invoke({"job_description": str(result), "link_list": links})

print(email_result.content)
```

### **5️⃣ Deploy with Streamlit**
```python
streamli run main.py
```

---

## **🔹 Technologies Used**  
✅ **LangChain** → Extracting job data & structuring responses  
✅ **ChromaDB** → Storing & retrieving job information efficiently  
✅ **ChatGroq (LLM)** → Generating structured data & personalized cold emails  
✅ **Streamlit** → Deploying an interactive web app  
✅ **Prompt Engineering & Chaining** → Automating workflow  

---

## **🚀 Outcome**  
By combining **LLMs, vector databases, and Streamlit**, this system provides a **fully automated cold email generation tool** that is easy to use and deploy. 🚀  

Let me know if you need further refinements! 😊
