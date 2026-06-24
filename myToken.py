from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer 
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

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

#wordpunct_tokenize
wordpunct_corp = wordpunct_tokenize(corpus)
print("corp to wordpunct: ",wordpunct_corp) # "'s" is divided into two tokens: "'" and "s"
print("--------------------------------")

#TreebankWordTokenizer
treebank_tokenizer = TreebankWordTokenizer()
treebank_corp = treebank_tokenizer.tokenize(corpus)
print("corp to treebank: ",treebank_corp) # "'s" is not divided into two tokens: "'" and "s"
#"." in the middle of the sentence is not divided into two tokens: "e.g." is one token 
# whereas the last "." is divided into two tokens: "e.g" and "." 
print("--------------------------------")

#STEMMING
print("PorterStemmer >>>")
ps = PorterStemmer()
words = ["running", "ran", "runs", "easily", "eats","finalized","finally"]
for w in words:
    print(w, " : ", ps.stem(w))
print("SnowballStemmer >>>")
ss = SnowballStemmer("english")
for w in words:
    print(w, " : ", ss.stem(w))
print("--------------------------------")

#RegexStemmer
print("RegexpStemmer")
rs = RegexpStemmer('ing$|s$|e$|able$', min=2)
words = ["running", "ran", "runs", "easily", "eats","finalized","finally"]
for w in words:
    print(w, " : ", rs.stem(w))
print("--------------------------------")