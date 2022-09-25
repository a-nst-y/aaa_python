class CountVectorizer:

    """Convert a collection of text"""

    def __init__(self, lowercase=True):
        self.lowercase = lowercase

    def fit_transform(self, corpus):
        """Transform a corpus of text to a document-term matrix"""
        if self.lowercase == True:
            corpus = [words.lower() for words in corpus]

        feature_names = list(set(sum([sent.split() for sent in corpus], [])))
        self.feature_names = feature_names

        doc_matrix = []
        for sent in corpus:
            sent.split()
            features_freq = []
            for feature in feature_names:
                feature_count = sent.count(feature)
                features_freq.append(feature_count)
            doc_matrix.append(features_freq)
        return doc_matrix

    def get_feature_names(self):
        return self.feature_names


if __name__ == "__main__":
    some_text = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(some_text)
    print(vectorizer.get_feature_names())
    print(count_matrix)
