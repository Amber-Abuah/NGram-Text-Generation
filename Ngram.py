import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from nltk.corpus import gutenberg

nltk.download('gutenberg')
nltk.download('punkt_tab') 

all_text = ""
for file_id in gutenberg.fileids()[:2]:
    all_text += gutenberg.raw(file_id)

sentences = [word_tokenize(sent.lower()) for sent in sent_tokenize(all_text)]

def build_model(N):
    train_data, vocab = padded_everygram_pipeline(N, sentences)
    train_data = [[ngram for ngram in sentence_ngrams if "<s>" not in ngram and "</s>" not in ngram]  for sentence_ngrams in train_data] # Remove <s> and </s> symbols
    model = MLE(N)
    model.fit(train_data, vocab)
    return model

bigram_model = build_model(2)
trigram_model = build_model(3)
fourgram_model = build_model(4)
print("Created N-grams successfully.")

def predict_next_word(context, N, num_words=1):
    context_tokens = word_tokenize(context.lower())
    model = bigram_model if N == 2 else trigram_model if N == 3 else fourgram_model
    prediction = model.generate(num_words, context_tokens)

    # If array, convert to single string
    if type(prediction) != str:
        prediction = " ".join(prediction)

    return prediction

context = "I was in awe when I noticed"
print("Bigram:", context, predict_next_word(context, 2, 10))
print("Trigram:", context, predict_next_word(context, 3, 15))
print("Fourgram:", context, predict_next_word(context, 4, 20))