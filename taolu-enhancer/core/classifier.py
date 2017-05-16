'''
	This file contains the implementation of the SVM classification algorithm for detecting specific poses based on angle features.
	The support vectors are carefully selected feature points, each representing a specific image.
'''
from sklearn import svm

class SVMClassifier:

	# Initialize the classifier. This class expects the support vectors to be provided externally
	def __init__(self, sv=None):
		self.support_vectors = sv

	# Train the classifier
	def trainSVM(self):
		pass