# Movie Review Sentiment Analysis

## Working Project : https://moviereviewsentimentanalysis.streamlit.app/

## Overview

A sentiment analysis tool that predicts whether a given movie review is positive or negative.
The model is trained on a dataset from IMDB containing 50,000 labeled reviews and achieves an accuracy of 90%.

## Features

- **Sentiment Prediction**: Enter a movie review and get a sentiment prediction - either positive or negative.

## Technical Details

### Data

- **Dataset**: IMDB dataset
- **Number of reviews**: 50,000 (labeled)
- **Data Source**: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

### Tools and Libraries

- **Languages**: Python
- **Libraries**: 
  - Pandas
  - NumPy
  - Scikit-learn
- **Model**:
  - Preprocessing: TF-IDF Vectorization
  - Algorithm: Linear Support Vector Classifier (LinearSVC)

### Model Performance

- **Accuracy**: 90%
- **Precision**: 0.90(for both Positive and negative)
- **Recall**: 0.89(for Negative) and 0.91 (for Positive)
- **f-1 score**: 0.90(for both Positive and negative)

## Getting Started

If you'd like to run the project locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Mayank-bhardwaj02/MovieReviewSentimentAnalysis.git
    ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run Streamlit App**:
    ```bash
    streamlit run Movieapp.py
    ```


