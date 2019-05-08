from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt

class _Estimator:
    ## Contructor of the _Estimator class
    # @param min_cat is an integer value which defines the minimal number of categories
    # @param max_cat is an integer value which defines the maximal number of categories
    def __init__(self, max_cat=20):
        self._min_cat = 2
        self._max_cat = max_cat

    def _estimateNumberOfCategories(self, dataset):
        errors = []
        for i in range(self._min_cat, self._max_cat):
            kmeans = KMeans(n_clusters=i, n_jobs=-1)
            kmeans.fit(dataset)
            errors.append(kmeans.inertia_)
        return next(i + self._min_cat + 1 for i in range(len(errors)) if (errors[i] - errors[i-1])/errors[0] < .05)

    def getPositionOfMinerals(self, dataset):
        kmeans = KMeans(n_clusters=self._estimateNumberOfCategories(dataset), n_jobs=-1)
        kmeans.fit(dataset)
        return kmeans.cluster_centers_

