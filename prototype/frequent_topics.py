from gensim import corpora, models
from gensim.matutils import Sparse2Corpus
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
import spacy
from unidecode import unidecode

nlp = spacy.load("pt_core_news_sm")
class CommentsAnalyzer:

    def __init__(self, feedbacks):
        nltk.download('stopwords')
        self.stop_words = stopwords.words('portuguese')
        self.feedbacks = self.filter_by_pos(feedbacks)
        self.vectorizer = CountVectorizer(stop_words=self.stop_words)
        self.X, self.terms = self.preprocess_data()
        self.corpus = Sparse2Corpus(self.X, documents_columns=False)
        self.dictionary = corpora.Dictionary.from_corpus(self.corpus, id2word=dict((id, word) for word, id in self.vectorizer.vocabulary_.items()))

    def filter_by_pos(self, texts):
        """Processa os comentários e mantém apenas substantivos e adjetivos"""
        filtered_texts = []
        for text in texts:
            doc = nlp(text)
            tokens = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "ADJ"] and len(token.lemma_)>3]
            filtered_texts.append(" ".join(tokens))
        return filtered_texts

    def preprocess_data(self):
        X = self.vectorizer.fit_transform(self.feedbacks)
        return X, self.vectorizer.get_feature_names_out()


    def get_keyword_frequencies(self, num_topics=8):
        lda = models.LdaModel(self.corpus, num_topics=num_topics, id2word=self.dictionary, passes=15, random_state=10)
        
        # Pegar as principais palavras-chave de cada tópico
        keywords = []
        for _, topic in lda.print_topics(-1):
            top_keyword = topic.split('+')[0].split('*')[-1].strip().replace('"', '')
            keywords.append(top_keyword)
        
        # Contar a frequência dessas palavras-chave em todo o corpus
        keyword_frequencies = dict.fromkeys(keywords, 0)
        for doc in self.feedbacks: 
            tokens = doc.split()
            for keyword in keywords:
                keyword_frequencies[keyword] += tokens.count(keyword)

        return keyword_frequencies


