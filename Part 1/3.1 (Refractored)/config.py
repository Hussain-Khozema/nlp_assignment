import os
import enum
import pandas as pd
import content_extractor
from statistics import median

FOLDERS = { "DOMAIN_FOLDER_NAME" : "Domains/","DATA_FOLDER" : "/data/", "URL_FOLDER" :"/url/", "OUTPUT_FOLDER" : "/output/"}
DOMAIN_URL_PREFIXES = {"domain-1": 'https://en.wikipedia.org/wiki/', 'domain-2': "https://millercenter.org/the-presidency/presidential-speeches/", 'domain-3': "https://stackoverflow.com/questions/"}

def getURLsSuffix(domain):
    sub_folder = FOLDERS["URL_FOLDER"]
    files = getFilesInDirectory(domain,sub_folder)
    all_urls = []
    for file in files:
        f = open(FOLDERS["DOMAIN_FOLDER_NAME"] + domain + sub_folder + file, "r")
        for i in f.read().strip().split(','):
            all_urls.extend([DOMAIN_URL_PREFIXES[domain] + i])
            createFile(FOLDERS["DOMAIN_FOLDER_NAME"] + domain + FOLDERS["DATA_FOLDER"] + i)

    return all_urls

def getFilesInDirectory(domain,sub_folder):
    files = os.listdir(FOLDERS["DOMAIN_FOLDER_NAME"] + domain + sub_folder)
    return files

def checkFileExists(domain,sub_folder,file_name):
    return os.path.isfile(FOLDERS["DOMAIN_FOLDER_NAME"] + domain + sub_folder + file_name)


def createFile(file_url):
    open(file_url, 'w').close()

def saveToDir(domain,df,file_name):
    df.to_csv(FOLDERS["DOMAIN_FOLDER_NAME"] + domain + FOLDERS['OUTPUT_FOLDER'] + file_name + '.csv', index = False, header=True)

def get_all_data(domain):
    return content_extractor.extract_content(domain)

def get_statistics(data_counter,data_collection,title):
    print(title + " Statistics")
    print("--------------------------------------")
    sum_of_numbers = sum(number*count for number, count in data_counter.items())
    count = sum(count for n, count in data_counter.items())
    mean = sum_of_numbers / count

    print("Mean: " + str(mean))
    print("Mode: " + str(data_counter.most_common(1)[0][0]))
    print(data_counter.most_common(1))
    print("Median: " + str(median(data_counter)))
