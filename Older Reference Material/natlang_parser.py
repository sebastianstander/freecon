#freecon_NLparse.py


# FLAGS
is_providing_feedback = False


# GLOBALS
sentimental_documents = []
sentiment_keywords_per_document = []
scored_sentiment =[]
current_document_index = 0 

def toggle_feedback() :
	is_providing_feedback = True if is_providing_feedback is True else False

def feedback(message) :
	if (is_providing_feedback) :
		print(message)

def parse_keywords() :
	feedback("raw text : ( {} )".format(keyword) in sentiment_keywords_per_document )

	feedback("keywords : ( {} )".format(keyword,score) in keyword_model )
def extract_features() :

	feedback("features found : ( {} )".format(feature) in document_features )

def train_naive_bayes_classifier() :


def test_classfier() :



## From : https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python
# Load and prepare the dataset
import nltk
import random

documents = [ ( list(movie_reviews.word(fileid)) , category ) 
				for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category) ]

# Feature Extractor
word_pile = nltk.FreqDist( wrd.lower() for wrd in movie_reviews.words() )
word_features = list(word_pile)[:2000]
def doctument_features( document ) :
	document_content = set(document)
	features = {}
	for word in word_features :
		features['found({})'.format(word)] = ( word in document_content )
	return features

# Train Naive Bayes Classifier
feature_sets = [ (document_features(doc),clss) for (doc,clss) in documents ]
training_set , testing_set = feature_sets[100:] , feature_sets [:100]
classifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the Classifier
print( nltk.classify.accuracy( classifier , test_set ) )

# Show the most important features as interpreted by Naive Bayes
classifier.show_most_informative_features(5)