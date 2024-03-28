import pandas as pd
import numpy as np
import re
from tqdm import tqdm
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import scipy.stats
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_stop
from sklearn.feature_extraction.text import CountVectorizer #tfidf fonctionne aussi
from bertopic import BERTopic
from umap import UMAP
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from datetime import datetime 



### Statistiques sur le texte

def convert_string_to_int(s):
    # Retire les espaces de la chaîne de caractères
    s = s.strip()
    try : 
        # Vérifie si la chaîne de caractères se termine par 'k'
        if s.endswith('k'):
            # Remplace 'k' par rien et multiplie par 1000
            return int(float(s[:-1]) * 1000)
        else:
            # Si pas de 'k', convertit simplement en entier
            return int(float(s))
    except : 
        return pd.NA
    
def clean_date(date_string):
    try:
        date_string = date_string.replace('this post was submitted on ', '').strip()
        return datetime.strptime(date_string, "%d %b %Y")
    except ValueError:
        return pd.NaT  
    

def nombre_de_mot(txt): 
    return len(txt.split(' '))

def longueur_phrase(txt): 
    phrases=txt.split('.')
    return np.mean([len(i.split(' ')) for i in phrases])

def type_token_ratio()


def lemmatizer(txt) : 
    nlp = spacy.load('fr_core_news_md')
    doc = nlp(self.txt)
    lemmes = ' '.join([token.lemma_ for token in doc])
    return lemmes


def type_token_ratio(txt) : 

    # Tokenisation des mots
    tokens = word_tokenize(txt)

    # Calcul du nombre total de mots et de mots uniques
    total_mots = len(tokens)
    mots_uniques = set(tokens)

    # Calcul de l'indice de token ratio
    indice_token_ratio = len(mots_uniques) / total_mots

    return indice_token_ratio

def calculate_lexical_entropy(text):
    # Diviser le texte en mots
    words = text.split()

    # Calculer la fréquence de chaque mot
    word_counts = Counter(words)

    # Calculer la probabilité de chaque mot
    total_words = len(words)
    word_probabilities = {word: count / total_words for word, count in word_counts.items()}

    # Calculer l'entropie lexicale
    lexical_entropy = -sum(prob * math.log(prob, 2) for prob in word_probabilities.values())

    return lexical_entropy

def CL_index(txt): 
    '''
    CLI=0,058*L - 0,296*S - 15,8 
    avec L le nombre moyen de lettre au 100 mots, S le nombre moyen de phrases par 100 mots
    '''
    # L= Lettres ÷ Mots × 100
    L = len(txt.split('')) / len(txt.split(' ')) * 100

    # S = Phrases ÷ Mots × 100
    S= len(txt.split('.')) / len(txt.split(' ')) * 100

    return 0.058 * L - 0,296 * S - 15,8 

def remove_outliers(df, column_name):
    # Calculate the first quartile (Q1) and third quartile (Q3)
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)

    # Calculate the interquartile range (IQR)
    IQR = Q3 - Q1
    print(IQR)

    # Define the lower and upper bounds to identify outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter the DataFrame to remove outliers
    df_filtered = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

    return df_filtered



