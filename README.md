# anime_rs
A Weighted Hybrid Anime Recommendation System combining Content-Based Filtering (FAISS) and Collaborative Filtering (ALS).

- **Content-Based Filtering (CBF)**: similarity search using **FAISS (Facebook AI Similarity Search)** search library.
- **Collaborative Filtering (CF)**: **ALS (Alternating Least Squares)** for predicting user ratings.
- **Hybrid Model**: weighted combination of CBF and CF with boosting for popularity and average ratings.
- **Cross-validation**: k-fold to evaluate system performance.


Due to size and licensing restrictions, **full datasets are not included**.

- **AniList API**: anime and user data must be fetched individually. Some attributes aren’t currently used, so queries can be simplified or the model further improved by using these additional fields.
- **Kaggle User Animelist Dataset**: ratings data, licensed under **CC BY 4.0**, by Ramazan Turan. Needs both, ratings.csv (for model) and animes.csv (for mapping):
https://doi.org/10.34740/kaggle/dsv/12962435

- **Note:** To fully reproduce results, you must fetch and prepare the full datasets.
