import glob
import numpy as np
import os
import pandas as pd
from global_setting import SCORE_FOLDER
from sklearn.metrics import f1_score
from scipy import spatial
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import warnings
import seaborn as sn
import sklearn.exceptions
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)


def word_occur_evaluation(word_occur_dictionary):
    word_occur_combined_list = []
    for key in word_occur_dictionary.keys():
        word_occur_combined_list.append(word_occur_dictionary[key])
    word_occur_combined = np.sum(word_occur_combined_list, axis=0)
    word_occur_fig = plt.figure(1, figsize=(12, 8))
    plt.hist(word_occur_combined, density=True, bins=30)
    plt.ylabel('word_occurrence')

    return word_occur_fig


def score_evaluation(score_dictionary, tone):
    score_combined_list = []
    for key in score_dictionary.keys():
        score_combined_list.append(score_dictionary[key])
    score_combined = np.sum(score_combined_list, axis=0)
    score_fig = plt.figure(2, figsize=(12, 8))
    plt.hist(score_combined, density=True, bins=30)
    plt.ylabel('score')

    real_tone = tone
    predicted_tone = []
    for score in score_combined:
        if score > 0:
            predicted_tone.append('positive')
        elif score < 0:
            predicted_tone.append('negative')
        else:
            predicted_tone.append('neutral')
    classification_matrix = classification_report(real_tone, predicted_tone)
    f1_scalar = f1_score(real_tone, predicted_tone, average='weighted')

    return score_fig, classification_matrix, f1_scalar


def similarity_evaluation(word_occur_dictionary):
    key_list = list(word_occur_dictionary.keys())
    similarity_list = []
    for i in range(len(key_list)):
        for j in range(len(key_list)):
            similarity = 1 - spatial.distance.cosine(word_occur_dictionary[key_list[i]], word_occur_dictionary[key_list[j]])
            similarity_list.append(similarity)
    similarity_matrix = np.array(similarity_list).reshape(len(key_list), len(key_list))
    similarity_df = pd.DataFrame(similarity_matrix, columns=key_list, index=key_list)

    similarity_fig = plt.figure(3, figsize=(12, 8))
    sn.heatmap(similarity_df, annot=True)
    plt.show()

    return similarity_fig, similarity_df
