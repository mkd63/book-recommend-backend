from books.models import Books
from .models import Ratings
from django_pandas.io import read_frame
import matplotlib.pyplot as plt
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

corrMatrix = pd.DataFrame()
def standardize(row):
    new_row = (row - row.mean())/(row.max()-row.min())
    return new_row

def get_similar(book_name, rating,corrMatrix):
    similar_score = corrMatrix[book_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_score

def recommend(user,input):
    all_books = Books.objects.all()
    all_ratings = Ratings.objects.all()
    # for i,rating in enumerate(all_ratings):
    #     b = rating.get("book_id")
    #     rating["book_id"] = b.id
    #     all_ratings[i] = rating

    books = read_frame(all_books)
    ratings_df = read_frame(all_ratings)
    books_df = books.rename(columns = {'name': 'book'}, inplace = False)
    print(ratings_df)
    print(books_df.head())
    ratings = pd.merge(ratings_df, books_df, on = 'book')
    ratings = pd.DataFrame(data = ratings)
    print(ratings.head())
    ratings = ratings_df.pivot(index='user', columns='book', values='rating')
    print(ratings.head())
    ratings.fillna(0, inplace=True)

    print(ratings.head())
    df_std = ratings.apply(standardize).T
    df_std.fillna(0, inplace=True)

    print(df_std)
    sparse_df = sparse.csr_matrix(df_std.values)
    print(sparse_df)
    corrMatrix = pd.DataFrame(cosine_similarity(sparse_df),index=ratings.columns,columns=ratings.columns)
    print(corrMatrix)
    corrMatrix = ratings.corr(method='pearson')
    print(corrMatrix.index.names)
    similar_scores = pd.DataFrame()
    for book,rating in input:
        similar_scores = similar_scores.append(get_similar(book,rating,corrMatrix),ignore_index = True)


    print(similar_scores.sum().sort_values(ascending=False))
    return similar_scores.sum().sort_values(ascending=False)
