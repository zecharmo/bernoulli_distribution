# a simple Bernoulli Naive Bayes model using NYT articles

# create urls to perform search on each of the Arts, Business, Obituaries, Sports, and World sections
urlArts = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?[facet_field=section_name=Arts]&api-key=key'
urlBiz = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?[facet_field=section_name=Business)]&api-key=key'
urlObit = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?[facet_field=section_name=Obituaries]&api-key=key'
urlSports = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?[facet_field=section_name=Sports]&api-key=key'
urlWorld = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?[facet_field=section_name=World]&api-key=key'
# replace key above with your API key

# create database and connect
con = lite.connect('articles.db')
cur = con.cursor()

# create a table to store information about each article
# the first column is the article URL, the second is the article title, and the third is the body returned by the API
with con:
    cur.execute('CREATE TABLE articles_arts (id INT PRIMARY KEY, article_url TEXT, article_title TEXT, body TEXT )')
	cur.execute('CREATE TABLE articles_biz (id INT PRIMARY KEY, article_url TEXT, article_title TEXT, body TEXT )')
	cur.execute('CREATE TABLE articles_obit (id INT PRIMARY KEY, article_url TEXT, article_title TEXT, body TEXT )')
	cur.execute('CREATE TABLE articles_sports (id INT PRIMARY KEY, article_url TEXT, article_title TEXT, body TEXT )')
	cur.execute('CREATE TABLE articles_world (id INT PRIMARY KEY, article_url TEXT, article_title TEXT, body TEXT )')

# for loop to get 2000 articles from for each of the Arts, Business, Obituaries, Sports, and World sections
for i in range(2000):
    r = requests.get(urlArts)

    cur.execute('INSERT INTO articles_arts VALUES (?),(?),(?)', article_url, article_title, body)
    con.commit()

for i in range(2000):
    r = requests.get(urlBiz)

    cur.execute('INSERT INTO articles_biz VALUES (?),(?),(?)', article_url, article_title, body)
    con.commit()
	
for i in range(2000):
    r = requests.get(urlObit)

    cur.execute('INSERT INTO articles_obit VALUES (?),(?),(?)', article_url, article_title, body)
    con.commit()

for i in range(2000):
    r = requests.get(urlSports)

    cur.execute('INSERT INTO articles_sports VALUES (?),(?),(?)', article_url, article_title, body)
    con.commit()

for i in range(2000):
    r = requests.get(urlWorld)

    cur.execute('INSERT INTO articles_world VALUES (?),(?),(?)', article_url, article_title, body)
    con.commit()

# a simple Bernoulli Naive Bayes model using these articles
# each article type can be considered a class, for example, Arts = 0, Business = 1, etc.
# we want to see what words in an article are most useful in predicting the article type
# we train by counting words and documents within the classes to estimate p(class) and p(word|class)
# we want to obtain p(class|word) and weight the hyperparameters α and β to reflect the words most useful in predicting the article type

# p(class|word) = (njc + α - 1) / (nc + α  + β - 1)
# njc = number of times a word appears in articles of a class
# nc = number of articles in the class

# the code should read the title and body text for each article 
# the training phase of the code should use the articles to estimate the weights taking the hyperparameters α and β as input
# the prediction phase should then accept these weights as inputs and output posterior probabilities for each class

# create a training data set on a randomized 50/50 train/test split of the data
dfTrain, dfTest = train_test_split(df, test_size=0.5)

# this is the subset of labels for the training set
cl = dfTrain[:,5]
# subset of labels for the test set, we're withholding these
true_labels  dfTest[:,5]
# run the model on the training set

# Comments on the effects of changing α and β:
# α and β are meant to smooth the parameter estimates
# increasing their values draws the distribution closer to a uniform distribution
# it has the effect of adding extra samples to the data

