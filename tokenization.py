import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

# Kullanıcıdan metin al
text = input("Bir cümle girin: ")

# Tokenization işlemi
word_tokens = word_tokenize(text)  # Kelime bazlı
sent_tokens = sent_tokenize(text)  # Cümle bazlı

print("Kelime Tokenleri:", word_tokens)
print("Cümle Tokenleri:", sent_tokens)
