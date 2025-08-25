import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import TOKENIZER_MODELS
import utils.llm_helpers as llm_helpers
import utils.tokenizer_helpers as tokenizer_helpers
import utils.enriched_prompts as enriched_prompts


def compare_models(prompt: str, analysis_type: str = "generation", enriched_prompt: str = None):

    try:
        final_prompt = enriched_prompt if enriched_prompt else prompt
        
        print(f"Comparing OpenAI and Gemini for {analysis_type.upper()}:")
        print("="*60)
        
        resGemini = llm_helpers.callGemini(final_prompt)
        resOpenai = llm_helpers.callOpenai(final_prompt)
        
        print(f"\n{analysis_type.upper()} COMPARISON:\n")
        print("GEMINI RESULT:")
        print("-" * 40)
        print(resGemini['response'])
        print("\n")
        
        print("OPENAI RESULT:")
        print("-" * 40) 
        print(resOpenai['response'])
        print("\n")
        
        # Tokenization Analysis
        print("TOKENIZATION ANALYSIS:")
        print("-" * 40)
        
        resTokenizer1 = tokenizer_helpers.show_tokens(final_prompt, TOKENIZER_MODELS[0])
        print(f"Model: {TOKENIZER_MODELS[0]}")
        print(resTokenizer1)
        print()
        
        resTokenizer2 = tokenizer_helpers.show_tokens(final_prompt, TOKENIZER_MODELS[1])
        print(f"Model: {TOKENIZER_MODELS[1]}")
        print(resTokenizer2)
        print()
        
        # Token Usage Comparison
        print("TOKEN USAGE COMPARISON:")
        print("-" * 40)
        
        if 'token_usage' in resGemini:
            statsGemini = resGemini['token_usage']
            print(f"GEMINI TOKENS:\n{statsGemini}\n")
        
        if 'token_usage' in resOpenai:
            statsOpenai = resOpenai['token_usage']
            print(f"OPENAI TOKENS:\n{statsOpenai}\n")
        
        return {
            "analysis_type": analysis_type,
            "original_prompt": prompt,
            "final_prompt": final_prompt,
            "gemini_result": resGemini,
            "openai_result": resOpenai,
            "tokenizer_results": {
                TOKENIZER_MODELS[0]: resTokenizer1,
                TOKENIZER_MODELS[1]: resTokenizer2
            }
        }
        
    except Exception as e:
        print(f"Error in {analysis_type} comparison: {e}")
        return None

def compare_models_generation(prompt: str):
    return compare_models(prompt, "generation")

def compare_models_summarization(prompt: str):
    enriched_prompt = enriched_prompts.get_summarization_prompt(prompt)
    return compare_models(prompt, "summarization", enriched_prompt)

def compare_models_sentiment_analysis(prompt: str):
    enriched_prompt = enriched_prompts.get_sentiment_analysis_prompt(prompt)
    return compare_models(prompt, "sentiment_analysis", enriched_prompt)

def compare_models_writing_style(prompt: str):
    enriched_prompt = enriched_prompts.get_writing_style_analysis_prompt(prompt)
    return compare_models(prompt, "writing_style", enriched_prompt)

def compare_models_language_detection(prompt: str):
    enriched_prompt = enriched_prompts.get_language_detection_prompt(prompt)
    return compare_models(prompt, "language_detection", enriched_prompt)

def compare_models_text_statistics(prompt: str):
    enriched_prompt = enriched_prompts.get_text_statistics_prompt(prompt)
    return compare_models(prompt, "text_statistics", enriched_prompt)

def compare_models_comprehensive(prompt: str):
    enriched_prompt = enriched_prompts.get_comprehensive_analysis_prompt(prompt)
    return compare_models(prompt, "comprehensive", enriched_prompt)


def compare_models_batch(prompts: list, analysis_type: str = "sentiment"):
    enriched_prompt = enriched_prompts.get_batch_processing_prompt(prompts, analysis_type)
    return compare_models(str(prompts), f"batch_{analysis_type}", enriched_prompt)

# Demo function to showcase all analysis types
def demo_all_comparisons():
    """Demonstrating all available model comparison functions"""
    sample_text = "The advancement of AI technology is both exciting and concerning for the future of work."
    
    print(" AVAILABLE COMPARISON FUNCTIONS:")
    print("="*50)
    
    functions = [
        ("Text Generation", compare_models_generation),
        ("Summarization", compare_models_summarization), 
        ("Sentiment Analysis", compare_models_sentiment_analysis),
        ("Writing Style", compare_models_writing_style),
        ("Language Detection", compare_models_language_detection),
        ("Text Statistics", compare_models_text_statistics),
        ("Comprehensive", compare_models_comprehensive)
    ]
    
    for name, func in functions:
        print(f"\n {name.upper()} COMPARISON")
        print("-" * 40)
        try:
            result = func(sample_text)
            if result:
                print("Analysis completed ")
            else:
                print(" Analysis failed")
        except Exception as e:
            print(f"Error: {e}")
        print()
    
    print("BATCH PROCESSING DEMO")
    print("-" * 40)
    batch_texts = [
        "I love this product!",
        "This service is disappointing.",
        "The weather is nice today."
    ]
    try:
        result = compare_models_batch(batch_texts, "sentiment")
        if result:
            print(" Batch analysis completed successfully")
        else:
            print(" Batch analysis failed")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    demo_all_comparisons()