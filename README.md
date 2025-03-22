# NLP Tokenization
Bu repository, Python'da Natural Language Processing (NLP) için temel tokenization işlemlerini gerçekleştiren bir örnek projedir. Tokenization, bir metni anlamlı parçalara ayırma işlemidir. Bu proje, verilen metnin kelime ve cümle bazında tokenlara ayrılmasını sağlar.

Proje Özeti
Bu Python kodu, nltk (Natural Language Toolkit) kütüphanesini kullanarak girilen metni kelime bazında (word_tokenize) ve cümle bazında (sent_tokenize) tokenize eder. Sonuç olarak, metnin her bir kelimesi ve cümlesi ayrı ayrı gösterilir.

Çalıştırma Adımları
Python ve Gerekli Kütüphaneleri Yükleme

Python'un yüklü olduğundan emin olun. Python 3.x sürümü önerilir.

nltk kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

bash
Copy
Edit
pip install nltk
nltk Veri Setlerini İndirme

Kodda kullanılan punkt verisi, cümle ve kelime tokenize işlemleri için gereklidir. Bu veri setini indirmek için şu komut kullanılır:

python
Copy
Edit
import nltk
nltk.download('punkt')
Bu komut, nltk'nin punkt veri setini indirir. İlk çalıştırmada bu işlemi yapmanız gerekebilir.

Kodu Çalıştırma

text değişkenine istediğiniz metni girin. Program, girilen metni hem kelime bazında hem de cümle bazında tokenize edecektir.

Kod Açıklaması
python
Copy
Edit
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk 'punkt' veri setini indirir
nltk.download('punkt')

# Kullanıcıdan metin al
text = input("Bir cümle girin: ")

# Kelime bazlı tokenizasyon
word_tokens = word_tokenize(text)

# Cümle bazlı tokenizasyon
sent_tokens = sent_tokenize(text)

# Sonuçları ekrana yazdırma
print("Kelime Tokenleri:", word_tokens)
print("Cümle Tokenleri:", sent_tokens)
word_tokenize: Metni kelimelere ayırır.

sent_tokenize: Metni cümlelere ayırır.

Örnek Çıktı
Girdi:

nginx
Copy
Edit
Bir Python projesi geliştirmek çok eğlenceli!
Çıktı:

less
Copy
Edit
Kelime Tokenleri: ['Bir', 'Python', 'projesi', 'geliştirmek', 'çok', 'eğlenceli', '!']
Cümle Tokenleri: ['Bir Python projesi geliştirmek çok eğlenceli!']
Katkıda Bulunma
Katkıda bulunmak isterseniz, önerilerinizi veya hataları GitHub issues bölümünde paylaşabilir veya pull request gönderebilirsiniz.

