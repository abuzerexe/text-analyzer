
# AI Text Analysis Tool

A comprehensive text analysis tool that leverages multiple Large Language Models (LLMs) and tokenizers to provide insights into text content. Built for the Buildables AI Fellowship Week 1 assignment.

## Features

### Core Features
- **Multi-Model Text Analysis**: Compare responses from Gemini and OpenAI models
- **Advanced Tokenization**: Analyze text using multiple tokenizer models (BERT, GPT-2, OPT)
- **Token Usage Tracking**: Monitor API usage and calculate costs
- **Comprehensive Comparisons**: Side-by-side analysis of different models

### Advanced Analysis Types
- **Text Summarization**: Generate concise summaries
- **Sentiment Analysis**: Detect emotional tone with confidence scores
- **Language Detection**: Identify languages and cultural context
- **Writing Style Analysis**: Assess formality, complexity, and tone
- **Text Statistics**: Readability scores and vocabulary analysis
- **Batch Processing**: Analyze multiple texts simultaneously

##  Installation

### Prerequisites
- Python 3.9+
- API keys for Gemini and OpenAI (via OpenRouter)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/abuzerexe/text-analyzer
cd text-analyzer
```

2. **Create virtual environment**
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Variables**
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
OPEN_ROUTER_KEY=your_openrouter_api_key_here
```

### API Key Setup
- **Gemini**: Get free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenRouter**: Sign up at [OpenRouter.ai](https://openrouter.ai/) for OpenAI model access

## 💻 Usage

### Quick Demo
Run all available analysis types:
```bash
python main.py
```

### Programmatic Usage
```python
from utils.compare_models import compare_models_sentiment_analysis

# Analyze sentiment
result = compare_models_sentiment_analysis("I love this product!")
print(result)
```

## Project Structure

```
text-analyzer/
├── README.md
├── requirements.txt
├── config.py                    # Configuration and API keys
├── main.py                     # Entry point
├── utils/
│   ├── __init__.py
│   ├── llm_helpers.py          # LLM API wrappers
│   ├── tokenizer_helpers.py    # Tokenization analysis
│   ├── compare_models.py       # Model comparison logic
│   └── enriched_prompts.py     # Specialized prompts
```

##  Configuration

Key settings in `config.py`:

```python
# Model Configuration
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"
DEFAULT_OPENAI_MODEL = "openai/gpt-4o"
MAX_TOKENS = 2000

# Tokenizer Models for Comparison
TOKENIZER_MODELS = [
    "bert-base-uncased",
    "gpt2",
    "facebook/opt-350m"
]
```

##  Analysis Types

### 1. Text Summarization
- Generates concise summaries maintaining key information
- Compares summary quality across models

### 2. Sentiment Analysis
```
Sentiment: positive/negative/neutral
Confidence Score: 0.0-1.0
Reasoning: Brief explanation
```

### 3. Language Detection
- Primary language identification
- Cultural context analysis
- Mixed language detection

### 4. Writing Style Analysis
- Formality level assessment
- Complexity scoring (1-10)
- Tone and audience identification

### 5. Text Statistics
- Word count and readability scores
- Vocabulary richness analysis
- Flesch-Kincaid grade level

### 6. Tokenization Comparison
- Multi-model token boundary analysis
- Vocabulary size comparisons
- Token efficiency metrics

##  Token Usage & Costs

The tool tracks:
- Input and output token counts
- Cost estimation per API call
- Usage statistics across models

## Dependencies

- `google-generativeai`: Gemini API access
- `openai`: OpenAI API client
- `transformers`: Hugging Face tokenizers
- `python-dotenv`: Environment variable management

##  Assignment Context

This project demonstrates understanding of:
- Large Language Model APIs and usage patterns
- Tokenization strategies across different model architectures
- Multi-model comparison and evaluation
- Production-ready Python application structure
- Error handling and cost optimization

---

