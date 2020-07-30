# importing tfidf vectorizer and kmeans function
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Creating a Tdidf table
vectorizer = TfidfVectorizer()

# receives a list
X = vectorizer.fit_transform(df.text_stem.values)

# setting the kmeans function
true_k = 7
model = KMeans(n_clusters=true_k,
              init='k-means++',
              max_iter=100,
              n_init=3,
              verbose=True)

model.fit(X)

# get the features and the centroids
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

for i in range(true_k):
    print("Cluster %d:" %i),
    for ind in order_centroids[i, :10]:
        print("%s" %terms[ind])

print("\n")
print("Prediction")
X = vectorizer.transform(['namorar ficar sexo relacionamento'])

predicted = model.predict(X)
print(predicted)

# apply the model to the data
b = vectorizer.transform(list(df.text_stem))

# predict the labels
b_predict = model.predict(b)

b_predict
