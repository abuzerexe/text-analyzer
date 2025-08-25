from transformers import AutoTokenizer

#  Using hugging face tokenizers

try:
    def show_tokens(sentence: str, name: str):
        
        tokenizer = AutoTokenizer.from_pretrained(name)

        v_len = len(tokenizer) # total length of this models vocabulary 
        token_ids = tokenizer(sentence).input_ids

        # print("Decoded Values of token: ")
        # for idx,token in enumerate(token_ids):
        #     print(tokenizer.decode(token))
        
        tokenizer_info = {
            "model_name": name,
            "vocab_len_of_model": v_len,
            "token_ids": token_ids,
            "token_ids_len": len(token_ids)
        }

        return tokenizer_info
    
except Exception as e:
    print(e)
    pass



