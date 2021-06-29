from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import difflib

#read the preprocessed dataset 
data = pd.read_csv('datasets\movie_final.csv')

#create objects 
vec = CountVectorizer()
#use fit tranform
vec_matrix = vec.fit_transform(data['combined'])
similarity = cosine_similarity(vec_matrix)

#define a function
def recommend_movie(movie):
    if movie not in data['movie_title'].unique():
        return []
    else:
        i = data.loc[data['movie_title'] == movie].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, Key=lambda x: x[1], reverse=True)
        lst = lst[1:11]
        result = []
        for i in range(len(lst)):
            a = lst[i][0]
            result.append(data['movie_title'][a])
        return result

