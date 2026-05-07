import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer

# Downloads
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.tokenizer = TreebankWordTokenizer()

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""

        text = text.lower()

        text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        # ✅ SAFE TOKENIZATION (NO punkt, NO punkt_tab)
        tokens = self.tokenizer.tokenize(text)

        cleaned_tokens = [
            self.stemmer.stem(token)
            for token in tokens
            if token not in self.stop_words and token.isalpha()
        ]

        return " ".join(cleaned_tokens)

text_cleaner = TextCleaner()