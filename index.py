from heapq import nlargest
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from string import punctuation

text=""
nltk.download('punkt_tab')
nltk.download('stopwords')

#read file
with open(r"C:\Users\NANDULA SINDHURA\Documents\sample.txt",'r') as file:
    text=file.read()



#Converting into lower
text=text.lower()




#sentence tokenization
sentences=sent_tokenize(text)
print(sentences)




#Word tokenization
words = [word_tokenize(sentence) for sentence in sentences]


#Flatten the list of words
words = [word for sublist in words for word in sublist]
print(words)


#Remove stopwords and puncutuation
stop_words=set(stopwords.words("english")+list(punctuation))

words=[word for word in words if word not in stop_words]

#Calculating word frequency
word_frequencies=nltk.FreqDist(words)



# Calculate sentence scores based on word frequencies
sentences_score={}

for sentence in sentences:
    for word in word_tokenize(sentence):
        if word in word_frequencies:
            if sentence not in sentences_score:
                sentences_score[sentence]=word_frequencies[word]
            else:
                sentences_score[sentence] += word_frequencies[word]
print(sentences_score)

# Get the top 3 sentences with highest scores as the summary
summary_sentences=nlargest(3,sentences_score,key=sentences_score.get)

# Generate summary
summary="".join(summary_sentences)
print("hi")
print(summary)
