import nltk
from nltk.stem import PorterStemmer
import config
import random
import pandas as pd
def pos_tag(domain,sentences):
    sentences_idx = random.sample(range(1, len(sentences)), 3)
    sentences_to_tag = [sentences[sentence] for sentence in sentences_idx]
    print("\n")

    all_pos_tags = []

    for sentence in sentences_to_tag:
        pos_tags = nltk.pos_tag(nltk.word_tokenize(sentence))
        pos_tags = [pos_tags[i] + (sentence,) for  i in range(len(pos_tags))]
        all_pos_tags.extend(pos_tags)
        print("POS Tagging:\b")
        print("Sentence: " + sentence + "\b")
        for pos in pos_tags:
            print(pos[:2])
        print("\n")

    pos_tag_df = pd.DataFrame.from_records(all_pos_tags, columns =['Word', 'POS-tag','Sentence'])
    config.saveToDir(domain,pos_tag_df,domain + "_pos-tag")
    print("\n")
    print("All Outputs has been saved to " + config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["OUTPUT_FOLDER"])
