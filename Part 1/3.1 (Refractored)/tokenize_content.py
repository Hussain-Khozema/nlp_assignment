import nltk
import config
import pandas as pd
import plotter
from collections import Counter

def tokenize(domain,all_data,stemming,show_stats = True):
    tokens_data = {}
    len_dist = {}
    all_data_str = ""
    print("\n")

    for i in all_data:
        all_data_str += i['text'] + " "

    print("Tokenizing data (" + stemming + ") for " + domain + "........")
    
    tokens = set(nltk.word_tokenize(all_data_str))
    for t in tokens:
        if(t not in tokens_data.keys()):
            tokens_data[t] = len(t)
        if(len(t) not in len_dist.keys()):
            len_dist[len(t)] = [t]
        else:
            len_dist[len(t)].append(t)

    print("Tokenizing data (" + stemming + ") Completed")
    print("\n")

    tokens_data_df = pd.DataFrame(tokens_data.items(), columns=['Token', 'Length'])
    len_dist_df = pd.DataFrame(len_dist.items(), columns=['Length', 'Tokens'])

    if not show_stats:
        return tokens_data, len_dist

    print("Total Tokens (" + stemming + "): " + str(len(tokens))) 
    print("All Tokens (" + stemming + ")")
    print("--------------------------------------")
    print(tokens_data_df)

    print("\n")
    print("Tokens grouped by length (" + stemming + ")")
    print("--------------------------------------")
    print(len_dist_df)

    print("\n")

    tokens_len_collection = []
    for key in tokens_data:
        tokens_len_collection.append(tokens_data[key])
    
    tokens_len_counter = Counter(tokens_len_collection)

    config.get_statistics(tokens_len_counter,tokens_len_collection,"Token (" + stemming + ")")

    print("All Outputs has been saved to " + config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["OUTPUT_FOLDER"])

    config.saveToDir(domain,tokens_data_df,domain + "_" + "all_tokens ("+ stemming + ")")
    config.saveToDir(domain,len_dist_df,domain + "_" + "all_tokens_grouped_by_length ("+ stemming +")")
    plotter.plot_single(domain,len_dist,"Token Distribution(" + stemming + ") - " + domain, "Length of Tokens","Number of Tokens")
