
# Experimenting Sentimental Analysis, Text Generation, zero-shot-classification through hugging face pipeline

from transformers import pipeline,AutoTokenizer,AutoModelForSequenceClassification

sentence = "i deserve this scholarship because"
modelname = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)

                                        #  sentiment analysis 

classifier = pipeline("sentiment-analysis", model=model,tokenizer=tokenizer)
res1 = classifier(sentence)


                                        #  text generation

generator = pipeline("text-generation",model=model,)
res2 = generator(
    sentence,
    max_length=50
)


generator = pipeline("zero-shot-classification")
res3 = generator("carbon diaoxide is a important thing.",
                candidate_labels = ["education","politics","science"])


print(res1)