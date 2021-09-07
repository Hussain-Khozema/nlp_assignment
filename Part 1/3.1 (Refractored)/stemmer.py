import nltk
from nltk.stem import PorterStemmer
import plotter
import config
import pandas as pd
from collections import Counter

def stem(domain,tokens_data_before,tokens_len_dist_before):
    tokens_data= {}
    len_dist = {}
    ps = PorterStemmer()

    print("\n")
    print("Stemming Data for " + domain + "........")

    for token in tokens_data_before.keys():
        stem = ps.stem(token)
        if(stem not in tokens_data.keys()):
            tokens_data[stem] = len(stem)
        if(len(stem) not in len_dist.keys()):
            len_dist[len(stem)] = [stem]
        else:
            len_dist[len(stem)].append(stem)

    print("Stemming Completed")
    print("\n")

    tokens_data_df = pd.DataFrame(tokens_data.items(), columns=['Token', 'Length'])
    len_dist_df = pd.DataFrame(len_dist.items(), columns=['Length', 'Tokens'])

    print("Total Tokens (After Stemming): " + str(len(tokens_data.keys()))) 
    print("All Tokens (After Stemming)")
    print("--------------------------------------")
    print(tokens_data_df)

    print("\n")
    print("Tokens grouped by length (After Stemming)")
    print("--------------------------------------")
    print(len_dist_df)

    print("\n")

    stem_collection = []
    for key in tokens_data:
        stem_collection.append(tokens_data[key])

    stem_counter = Counter(stem_collection)

    config.get_statistics(stem_counter,stem_collection,"Token (After Stemming)")

    print("\n")
    print("All Outputs has been saved to " + config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["OUTPUT_FOLDER"])

    config.saveToDir(domain,tokens_data_df,domain + "_" + "all_tokens (After Stemming)")
    config.saveToDir(domain,len_dist_df,domain + "_" + "all_tokens_grouped_by_length (After Stemming)")
    plotter.plot_single(domain,stem_counter,"Token Distribution (After Stemming) - " + domain, "Length of Tokens","Number of Tokens",True)
    plotter.plot_multiple(domain,stem_counter,tokens_len_dist_before,"Token Distribution (Before & After Stemming) - " + domain, "Length of Tokens","Number of Tokens")
