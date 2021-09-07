## Domain Specific Dataset Analysis
### Third Party Libraries
1. NLTK: https://www.nltk.org/install.html
2. pandas: https://pandas.pydata.org/docs/getting_started/install.html
3. Matplotlib: https://pypi.org/project/matplotlib/
4. Beautiful Soup: https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup

### Domains Selected
1. Chemical Elements (Wikipedia)
2. Presidental Speeches
3. Stackoverflow

### Directory Structure 
**1. Root/**
  - main.py 
    - Main executable code
  - web_scrapper.py
    - For performing **Web Scraping** based on selected domain
  - tokenize_content.py 
    - For permorming **Tokenization** based on selected domain
  - stemmer.py
    - For performing **Stemming** based on selected domain
  - sentence_segmentation.py
    - For performing **Sentence Segmentation** based on selected domain
  - pos_tagger.py
    - For performing **Pos Tagging** based on the selected domain
  - plotter.py 
    - Global functions for plotting of graphs to be used across domains
  - content_extracter.py
    - For extracting content from the scraped content based on selected domain
  - config.py
    - Global configurations parameters/functions to be used across domains
  
**2. Domains/**
  - **domain-1/**
    - **url/**
      - urls.txt 
        - All Domain 1's URLS *(comma-delimited)* to scrape content from.
    - **output/**
      - For storing all Domain 1's outputs by tasks executed 
    - **data/**
      - For storing all the data obtained from scraping Domain 1's URLS as provided in `urls.txt`
  - **domain-2/**
    - **url/**
      - urls.txt
        - All Domain 2's URLS *(comma-delimited)* to scrape content from.
    - **output/**
      - For storing all Domain 2's outputs by tasks executed 
    - **data/**
      - For storing all the data obtained from scraping Domain 2's URLS as provided in `urls.txt`
  - **domain-3/**
    - **url/**
      - urls.txt
        - All Domain 3's URLS *(comma-delimited)* to scrape content from.4
    - **output/**
      - For storing all Domain 3's outputs by tasks executed 
    - **data/**
      - For storing all the data obtained from scraping Domain 3's URLS as provided in `urls.txt`
      
### Executing the Code 
Using the command prompt _(Windows)_ or terminal _(linux)_ run the following command `python main.py -d <domain> -t <task>`
1. -d \<domain\> *[Required]*
  - **\<domain\>** accepts the following paramaters: `[domain-1, domain-2, domain-3]`
    1. The domain parameter provided is for specifying the domain to perform a task on.
       - e.g. domain-1 will means to perform a task on Domain 1.
2. -t \<task\> *[Required]*
  - **\<task\>** accepts the following paramaters: `[webscrape, tokenize, stem, sentence_segment, pos_tag]`
    1. `webscrape` carries out the **Web Scraping** task *(using web_scrapper.py)*
    2. `tokenize` carries out the **Tokenizing** task *(using tokenize_content.py)*
    3. `stem` carries out the **Stemming** task *(using stemmer.py)*
    4. `sentence_segment` carries out the **Sentence Segmentation** task *(using sentece_segmentation.py)*
    5. `pos_tag` carries out the **POS Tagging** task *(using pos_tagger.py)*

**Sample Execution Code** 
- Running `python main.py -d domain-1 -t tokenize`
  1. **Tokenizing** will be done on **Domain 1**
  2. All outputs produced by the tokenizing task will be stored under the **output folder** for **Domain 1**
