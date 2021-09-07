import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import config

def plot_single(domain,data,title,x_label,y_label,stemming=False):
    tokens_x = list(data.keys())
    
    if(stemming):
        tokens_y = list(data.values())
    else:
        tokens_y = list()
        for k,v in data.items():
            tokens_y.append(len(v))

    fig = plt.figure()
    plt.bar(tokens_x,tokens_y)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.savefig(config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS['OUTPUT_FOLDER'] + title)
    plt.show()

def plot_multiple(domain,data,data_bef_stem,title,x_label,y_label):
    tokens_x = list(data.keys())
    tokens_y = list(data.values())

    tokens_x_bef_stem = list(data_bef_stem.keys())
    tokens_y_bef_stem = list()
    for k,v in data_bef_stem.items():
        tokens_y_bef_stem.append(len(v))

    fig = plt.figure()
    plt.bar(tokens_x_bef_stem,tokens_y_bef_stem,label="Before Stemming")
    plt.bar(tokens_x,tokens_y,alpha=0.5,color='r',label="After Stemming")
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.legend()
    plt.savefig(config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS['OUTPUT_FOLDER'] + title)
    plt.show()

def plot_sentence(domain,data,title,x_label,y_label):
    sentences_y = list(data.values())
    sentences_x = list(data.keys())

    fig = plt.figure()
    plt.bar(sentences_x,sentences_y)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.savefig(config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS['OUTPUT_FOLDER'] + title)
    plt.show()
