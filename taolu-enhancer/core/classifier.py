'''
    This file contains the implementation of the SVM classification algorithm for detecting specific poses based on angle features.
    The support vectors are carefully selected feature points, each representing a specific image.
'''

from utils.db import getAnglesDB
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score


class SVMClassifier:

    # Initialize the classifier. This class expects the support vectors to be provided externally
    def __init__(self, sv=None):
        self.support_vectors = sv
        db_content = getAnglesDB()

        angles = list()
        labels = list()
        for c in db_content:
            _, *t = c
            labels.append(''.join([i for i in t[0] if not i.isdigit()]))
            angles.append(t[1:])

        np_angles = np.array(angles)
        np_labels = np.array(labels)

        self.clf = svm.SVC(decision_function_shape='ovr')
        self.clf.fit(angles, labels)

    # Train the classifier
    def guessValueSVM(self, angles):
        return self.clf.predict(angles)

    def getConfidence(self, angles):
        return self.clf.decision_function(angles)

    def getCrossValScore(self):
        db_content = getAnglesDB()
        angles = list()
        labels = list()
        for c in db_content:
            _, *t = c
            labels.append(''.join([i for i in t[0] if not i.isdigit()]))
            angles.append(t[1:])

        print(angles)
        print(labels)

        scores = cross_val_score(self.clf, angles, labels, cv=10)
        return (scores.mean(), scores.std() * 2)
