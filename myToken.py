from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

corpus = "Hello there, how are you? I am fine. Thank you for asking! Let's meet tomorrow."

sent_corp = sent_tokenize(corpus, language='english')
print("corp to sent: ",sent_corp)

word_corp = word_tokenize(corpus, language='english')
print("corp to word: ",word_corp)

for sent in sent_corp:
    word_sent = word_tokenize(sent, language='english')
    print("sent to word: ",word_sent)