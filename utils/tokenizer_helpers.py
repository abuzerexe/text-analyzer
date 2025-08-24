from transformers import AutoTokenizer

#  Using hugging face tokenizers

def show_tokens(sentence: str, name: str):
    
    tokenizer = AutoTokenizer.from_pretrained(name)

    print(f"Vocab length: {len(tokenizer)}")

    res = tokenizer(sentence)

    token_ids = tokenizer(sentence).input_ids
    print(f"token IDs: {token_ids}" )

    for idx,token in enumerate(token_ids):
        print(tokenizer.decode(token))