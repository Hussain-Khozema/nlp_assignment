import web_scraper
import tokenize_content
import content_extractor
import sentence_segmentation
import pos_tagger
import stemmer
import config
import os
import sys
import argparse

def webscrape(domain):
    web_scraper.scrape_web(domain)

def tokenize(domain):
    tokenize_content.tokenize(domain,config.get_all_data(domain),"Before Stemming")

def stem(domain):
    tokens_data, len_dist = tokenize_content.tokenize(domain,config.get_all_data(domain),"After Stemming",False)
    stemmer.stem(domain,tokens_data,len_dist)

def sentence_segment(domain):
    sentence_segmentation.segment_sentence(domain,config.get_all_data(domain))

def pos_tag(domain):
    pos_tagger.pos_tag(domain,sentence_segmentation.segment_sentence(domain,config.get_all_data(domain),True))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", required = True, help="Domain - [domain-1, domain-2, domain-3]")
    parser.add_argument("-t", "-task" , required = True, help="Task to Run - [webscrape,tokenize,stem,sentence_segment,pos_tag]")

    args = vars(parser.parse_args())
    globals()[args['t']](args["d"])

if __name__ == "__main__":
    main()
