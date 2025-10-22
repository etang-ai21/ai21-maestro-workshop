# Workshop Module: Maestro RAG with File Search

## What is Maestro RAG?

Maestro RAG (Retrieval-Augmented Generation) enables you to build conversational AI applications that answer questions grounded in your own documents. Instead of relying on the model's training data alone, Maestro retrieves relevant information from your files and uses it to generate accurate, source-backed responses.

**Key benefit**: Responses are grounded in your actual documents, eliminating hallucination and ensuring enterprise-grade accuracy.

## How It Works

Maestro combines AI21's advanced RAG Engine with a planning layer to enable:

1. **Multi-turn conversations**: Ask follow-up questions and get context-aware answers
2. **Semantic search**: Automatically finds relevant information across your document library
3. **Grounded responses**: Answers cite actual sources from your files
4. **Step-by-step reasoning**: Handles complex queries requiring information synthesis

## File Search Tool

The File Search tool enables Maestro to retrieve information from your uploaded documents through semantic search.

### Supported File Formats
- PDF
- DOCX
- TXT
- HTML
- Markdown

### How It Works
1. **Upload**: Add documents to your File Library
2. **Automatic indexing**: RAG Engine indexes your documents for semantic search
3. **Query**: Ask questions in natural language
4. **Retrieve & Generate**: Maestro finds relevant chunks and generates grounded answers

## When to Use RAG

### ✅ Ideal Use Cases
- **Internal knowledge bases**: Employee handbooks, technical documentation, policies
- **Customer support**: Product manuals, troubleshooting guides, FAQs
- **Research assistants**: Query large document collections
- **Compliance & legal**: Answer questions grounded in specific regulations or contracts
- **Onboarding tools**: Help new employees/users find information

### ❌ Less Suitable Use Cases
- General knowledge questions (no need for document retrieval)
- Creative writing without source material
- Real-time data requiring live updates

## Key Advantages

**Conversational Intelligence**
Go beyond single Q&A by supporting follow-up questions, clarifications, and multi-step problem-solving through natural dialogue.

**Enterprise-Grade Accuracy**
Built on RAG, responses are grounded in your actual documents with source citations, not model hallucinations.

**Fully Managed**
Simply upload your documents—the RAG Engine handles indexing automatically. No infrastructure setup required.

**Source Transparency**
Every answer includes references to the source documents, making it easy to verify and audit responses.

## Demo: Technical Troubleshooting Assistant

### The Use Case

We'll build an AI assistant that instantly troubleshoots technical issues using data from manuals, support records, and connected sources. It delivers accurate, sourced answers that reduce escalations, speed up resolutions, and improve customer support.

### Why Maestro RAG Matters Here

- Answers are grounded in your current internal knowledge
- Output structure matters
- Output content prioritization matters

### What You'll Build

In the modules notebook:
- Uploads technical documentation to the File Library
- Queries the content using different budget tiers
- Retrieves contextually relevant information
- Generates answers with source citations


---

**Next**: Hands-on coding with the AI21 Maestro RAG API