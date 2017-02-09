import unittest
from sklearn.datasets import make_multilabel_classification
from sklearn.model_selection import train_test_split

from skmultilearn.dataset import Dataset
from skmultilearn.ensemble.rakeld import RakelD
from skmultilearn.problem_transform import BinaryRelevance, LabelPowerset
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB

class MLClassifierBaseTests(unittest.TestCase):

    def test_model_selection_works(self):
        x, y = make_multilabel_classification(sparse=True, n_labels=5,
                                              return_indicator='sparse', allow_unlabeled=False)

        parameters = {
            'labelset_size': range(2, 3),
            'classifier': [LabelPowerset(), BinaryRelevance()],
            'classifier__classifier': [MultinomialNB()],
            'classifier__classifier__alpha': [0.7, 1.0],
        }

        clf = GridSearchCV(RakelD(), parameters, scoring='f1_macro')
        clf.fit(x, y)

        for p in parameters.keys():
            self.assertIn(p, clf.best_params_)

        self.assertIsNotNone(clf.best_score_)