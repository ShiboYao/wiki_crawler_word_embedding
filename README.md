**1. Introduction**\
Web-crawl Wikipedia pages about S&P500 companies, process the corpus, train word embedding on the corpus and evaluate the embedding via KNN classifier and visualization(using LLE to reduce the dim to 2). 


**2. Requirements**\
python 3.X

for grabing html and parsing contents:  
bs4, lxml, urllib

for extracting articles:  
newspaper3k

for preprocessing text and tokenization:  
C compiler

for training:  
Tensorflow 


**3. Usage**  
*Data Gathering*  
"crawl" folder. 

Can skip data gathering and start from preprocessing.  
"python extract_500urls.py"  
"python extract_children.py delay", e.g. "python extract_children.py 1" (delay stands for the delay between requests)  
"python url2article.py"


*Processing*\
"process" folder.

I compiled on Ubuntu Linux. You might need to compile it on your system. "gcc -o preprocess preprocess.c"

"./preprocess raw.txt"

The preprocessing contains several parts: remove [edit] and [reference] from wiki articles, remove punctuations, remove words containing non-ASCII characters, convert all upper cases to lower, tokenize n-gram, remove stopwords, remove extra whitespaces and save as "processed.txt".

If you want to customize the punctuation list, go to "nlt.h" and add/remove punctuations. Recompile.

You may adapt the n-gram list, which will later be converted to tokens, by making changes to the .csv file. Note that stopwords can vary to corpus theme(topic).

If you want to customize the stopword list, go to "stopwords.txt" and add/remove words. Note that a single "," is used as delimiter.

To take a look at any plain text, use "see" program. "./see START LENGTH".


*Training Word2Vec*  
"word2vec" folder.

Since we would like to see how the token frequency affects word embedding quality, we can construct a token frequency list via "python getFreq.py"(take a while, need to look over the corpus). 

After preprocessing, you can train the word2vec by "python word2vec_full.py" or "python word2vec_part.py". The word frequency threshold (in terms of S&p500 company name) is 40. 

It is strongly recommended to use GPU for training. It takes several hours to get satisfying result on NVIDIA GP100. 

To save terminal output to a file, run as "python fname.py |& tee log.txt" so that you can compare the result given different model settings. 


*Get Domain Affinity Matrix and Word Embedding Matrix*  
"matrices" folder. 

To get the word embedding matrix for S&P500 company names, run "python domain Mat.py", and then run "python semanticMat.py full" or "python semanticMat.py part". 


*Evaluation*  
"eval" folder.

The classifier is merely a K-Nereast-Neighborhood. 

run "python semanticVisual.py MATNAME" to see the result on original domain word embedding matrix.  
e.g. "python semanticVisual.py full". 


espoyao (at) gmail [dot] com
