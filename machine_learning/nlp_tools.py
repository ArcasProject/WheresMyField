from spacy.en import English
from nltk.corpus import stopwords
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import string

parser = English()

STOPLIST = set(stopwords.words('english') + list(ENGLISH_STOP_WORDS))
SYMBOLS = " ".join(string.punctuation).split(" ")
SPECIAL_CHAR = ["-", "'", "‘", ":", "-----", "---", '--', "...", "…", "“",
                "”", "–", "—"]


def clean_text(text):
    # get rid of newlines
    text = text.strip().replace("\n", " ").replace("\r", " ")
    text = text.strip().replace("\\", " ").replace("$", " ")

    # repla ce HTML symbols
    text = text.replace("&amp;", "and").replace("&gt;", ">").replace("&lt;",
                                                                     "<")

    # lowercase
    text = text.lower()

    return text


def tokenize_text(raw_text):
    raw_text = clean_text(raw_text)
    # spacy function to get tokens
    tokens = parser(raw_text)

    # lemmatize
    lemmas = []
    for tok in tokens:
        # if tok.like_num == False:
        lemmas.append(
            tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
    tokens = lemmas

    # remove stopwords & symbols
    tokens = [tok for tok in tokens if tok not in STOPLIST]
    tokens = [tok for tok in tokens if tok not in SYMBOLS]
    tokens = [tok for tok in tokens if tok not in SPECIAL_CHAR]

    # remove spaces if they exist
    while "" in tokens:
        tokens.remove("")
    while " " in tokens:
        tokens.remove(" ")
    while "\n" in tokens:
        tokens.remove("\n")
    while "\n\n" in tokens:
        tokens.remove("\n\n")

    return tokens
