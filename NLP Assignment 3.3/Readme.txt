
1. Third party libraries:
  - NLTK: https://www.nltk.org/install.html
  - re: https://pypi.org/project/regex/
  - numpy: https://numpy.org/install/
  - pandas: https://pandas.pydata.org/docs/getting_started/install.html
  - sklearn: https://scikit-learn.org/stable/install.html
  - pickle: https://pypi.org/project/pickle-mixin/

2. How to use sentiment_classifier.py?
  - Ensure sentiment_classifier.py is in the same folder as 'model' and 'vectorizer'
  - Open command prompt in windows or terminal in macOS
  - cd to the directory where sentiment.py is located at. eg: cd Desktop
  - type this following command: python sentiment_classifier.py
  - User will be prompt with "Please input your review:"
  - Type in review as requested and press 'enter' and the program will return the sentiment of the review

3. Explanation of sample output:
  - After user's review input, the program will return "Your review sentiment is: {Negative, Neutral, Positive}"
  - Other than returning the sentiment of the review, the program will return the confidence score.
  - Example: a confidence score of 0.9 will be better than 0.5.
