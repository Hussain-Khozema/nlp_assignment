import nltk
import config
import pandas as pd
import plotter
from nltk.tokenize import sent_tokenize
from collections import Counter
from statistics import median

def segment_sentence(domain,data,extract_sentences=False):

    sentences = list()
    for i in data:
        sentences.extend(sent_tokenize(i['text']))

    if(extract_sentences):
        return sentences

    print("\n")
    print("Segmenting Sentence for " + domain + "........")
    sentences_len_dist = []
    for s in sentences:
        sentence_token = nltk.word_tokenize(s)
        sentences_len_dist.append(len(sentence_token))

    print("\n")

    sentences_len_counter = Counter(sentences_len_dist)

    sentence_len_df = pd.DataFrame.from_dict(sentences_len_counter, orient='index').reset_index()
    sentence_len_df = sentence_len_df.rename(columns={'index':'Sentence Length', 0:'Count'})

    config.saveToDir(domain,sentence_len_df,domain + "_sentence-segmentation")

    config.get_statistics(sentences_len_counter,sentences_len_dist,"Segment Length")

    print("\n")
    print("All Outputs has been saved to " + config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["OUTPUT_FOLDER"])

    plotter.plot_sentence(domain,sentences_len_counter,"Sentence Segmentation (" + domain + ")", "Sentence Length","Number of Sentences")
