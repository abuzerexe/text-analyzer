import utils.llm_helpers as llm
from utils.tokenizer_helpers import show_tokens


res1 = llm.callGemini("who is the meaning of life?")
# print("from gemnini: "+ res1)
res2 = llm.callOpenai("what is the meaning of life?")
# print("from openai: "+ res2)

res3 = show_tokens("hello world","bert-base-cased")
print("token infoRES3: ")
print(res3)

res4 = show_tokens("hello world","Xenova/gpt-4")
print("token info RES4: ")
print(res4)
