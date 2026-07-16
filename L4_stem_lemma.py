from nltk.stem import PorterStemmer 
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

#PORTER STEMMER
print("---PorterStemmer---")
ps = PorterStemmer()
words = ["running", "ran", "runs", "easily", "eats","finalized","finally"]
for w in words:
    print(w, " : ", ps.stem(w))
print("*******************************")

#SNOWBALL STEMMER
print("---SnowballStemmer---")
ss = SnowballStemmer("english")
for w in words:
    print(w, " : ", ss.stem(w))
print("*******************************")

#REGEXP STEMMER
print("---RegexpStemmer---")
rs = RegexpStemmer('ing$|s$|ed$|able$', min=2)
words = ["running", "ran", "runs", "easily", "eats","finalized","finally"]
for w in words:
    print(w, " : ", rs.stem(w))
print("*******************************")

#LEMMATIZATION
print("---WordNetLemmatizer---")
wnl = WordNetLemmatizer()
words = ["running", "ran", "runs", "easily", "eats","finalized","finally"]
for w in words:
    print(w, " : ", wnl.lemmatize(w, pos='v')) # pos='v' indicates a verb
print("*******************************")