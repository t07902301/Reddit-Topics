# prompt: clean a string with spark by remove stopwords, punctuation, and perform tokenization

import findspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, lower, regexp_replace
from pyspark.ml.feature import StopWordsRemover, Tokenizer
import json
from pyspark.sql.types import ArrayType, StringType

# import io
# from flask import Flask, render_template, send_file
import requests

import logging
import sys
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_spark():
    findspark.init()
    spark = SparkSession.builder \
            .appName('testColab') \
            .getOrCreate()
    return spark

def download_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to download JSON file. Status code: {response.status_code}")
        return None
    
def get_reddit_data(url) -> list[dict]:
    # # Read Subreddit JSON (assuming it's in the correct location)
    # with open('content/cscareerquestions.json', 'r') as file:
    #     data = json.load(file)

    # Download the JSON file
    data = download_json(url)

    extracted_posts = [{'url': post['data']['url'], 'content': post['data']['title'] + ' ' + post['data']['selftext']} for post in data['data']['children']]
    return extracted_posts

def create_spark_dataframe(spark, data):
    # Create a DataFrame
    df = spark.createDataFrame(data)
    return df

def clean_text(df):
    # 1. Convert to lowercase
    df = df.withColumn("content", lower(col("content")))

    # 2. Remove punctuation
    df = df.withColumn("content", regexp_replace(col("content"), "[^a-zA-Z\\s]", ""))

    # 3. Tokenize
    tokenizer = Tokenizer(inputCol="content", outputCol="tokens")
    df = tokenizer.transform(df)

    # 4. Remove stop words
    remover = StopWordsRemover(inputCol="tokens", outputCol="cleaned_tokens")
    df = remover.transform(df)

    return df

# Custom UDF to filter words by length
def filter_short_words(words):
    return [word for word in words if len(word) > 3]  # Keep words longer than 2 characters

def get_long_tokens(df):
    filter_udf = udf(filter_short_words, ArrayType(StringType()))
    df = df.withColumn("long_tokens", filter_udf(col("cleaned_tokens")))
    return df

import nltk
if not nltk.download('punkt_tab'):
    nltk.download('punkt_tab')
if not nltk.download('averaged_perceptron_tagger_eng'):
    nltk.download('averaged_perceptron_tagger_eng')
if not nltk.download('tagsets'):
    nltk.download('tagsets')

def extract_nouns(tokens):
    # Perform POS tagging
    tagged_tokens = nltk.pos_tag(tokens)
    # Extract nouns based on POS tags (NN, NNS, NNP, NNPS)
    nouns = [word for word, pos in tagged_tokens if pos.startswith('NN')]
    return nouns

def get_noun_tokens(df):
    extract_nouns_udf = udf(extract_nouns, ArrayType(StringType()))
    df = df.withColumn("noun_tokens", extract_nouns_udf(col("long_tokens")))
    return df

from pyspark.sql.functions import explode, count
from pyspark.sql.functions import col

def get_token_freq(df):
    # Explode the filtered_tokens array into separate rows
    exploded_df = df.select("url", explode("noun_tokens").alias("token"))

    # Group by token and count occurrences
    token_counts = exploded_df.groupBy("token").agg(count("*").alias("frequency"))

    return token_counts
    
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_freq(token_counts, image_path):

    # Convert the Spark DataFrame to a Pandas DataFrame
    word_counts_pandas = token_counts.toPandas()

    # Create a dictionary of word frequencies
    word_freq = dict(zip(word_counts_pandas['token'], word_counts_pandas['frequency']))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    # Save WordCloud as an image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(image_path)

def main(download_url, image_path):
    data = get_reddit_data(download_url)
    logger.info("Pulled the Reddit data")
    spark = init_spark()
    logger.info("Starting the Spark session")
    df = create_spark_dataframe(spark, data)
    logger.info("Created the Spark DataFrame from the remote JSON file")
    df = clean_text(df)
    logger.info("Cleaned the text data")
    df = get_long_tokens(df)
    logger.info("Filtered out short tokens")
    df = get_noun_tokens(df)
    logger.info("Extracted noun tokens")
    token_counts = get_token_freq(df)
    logger.info("Calculated token frequencies")
    plot_freq(token_counts, image_path)
    logger.info(f"Plotted the word cloud and saved to {image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py <download_url> <image_path>")
        sys.exit(1)
    download_url = sys.argv[1]
    image_path = sys.argv[2]
    main(download_url, image_path)

# # Save WordCloud to an image buffer
# img_buffer = io.BytesIO()
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.savefig(img_buffer, format='png')
# img_buffer.seek(0)
# plt.close()


# # Flask App
# app = Flask(__name__)
# @app.route("/")
# def index():
#     return """
#         <html>
#             <body>
#                 <h1>Word Cloud Visualization</h1>
#                 <img src="/wordcloud" alt="Word Cloud">
#             </body>
#         </html>
#     """

# @app.route("/wordcloud")
# def wordcloud_image():
#     img_buffer.seek(0)  # Reset the buffer's pointer
#     return send_file(img_buffer, mimetype='image/png')

# if __name__ == "__main__":
#     app.run(debug=True)
