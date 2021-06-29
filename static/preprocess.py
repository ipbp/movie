import numpy as np 
import pandas as pd

#read dataset
data = pd.read_csv('datasets\movie_metadata.csv')

# dropping unnecessary columns 
data = data.drop([ 'color', 'num_critic_for_reviews',
       'duration', 'director_facebook_likes', 'actor_3_facebook_likes',
        'actor_1_facebook_likes', 'gross',
       'num_voted_users',
       'cast_total_facebook_likes', 'facenumber_in_poster',
       'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language',
       'country', 'content_rating', 'budget', 'title_year',
       'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio',
       'movie_facebook_likes'],axis=1)
#Text PreProcessing
data.dropna(inplace=True)

#clean genres remove | between genres
data['genres'] = data['genres'].apply(lambda a: str(a).replace('|',''))

#Clean movie_title Column
data['movie_title'] = data['movie_title'].apply(lambda a: a[:-1])

#combined features on which we will calculate cosine similarity
#data['combined']=data['director_name']+''+data['actor_2_name']+''+data['actor_1_name']+''+data['genres']+''+data['actor_3_name']
data['combined']=data['director_name']+' ' +data['actor_2_name']+' '+data['genres']+ ' ' +data['actor_1_name']+' '+data['actor_3_name']
#saving the preprocessed dataset
data.to_csv('datasets\movie_final.csv')