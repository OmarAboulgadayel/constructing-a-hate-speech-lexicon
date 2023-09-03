import yake
import csv

csv_file = ".\data\labeled_data.csv"

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    tweets = ""

    for row in reader:
        if row["class"] == "0":
            tweets += row["tweet"] + " "

max_ngram_size = 3
num_of_keywords = 300

kw_extractor = yake.KeywordExtractor(n=max_ngram_size, top=num_of_keywords)
keywords = kw_extractor.extract_keywords(tweets)

for kw in keywords:
    print(kw)
