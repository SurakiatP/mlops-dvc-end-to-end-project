import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def featurize(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Build target: Score >= 5 => 1, else => 0
    df["target"] = (df["Score"] >= 5).astype(int)

    # Prepare text columns.
    df["text"] = (
        df["Title"].fillna("") + " " +
        df["Tags"].fillna("") + " " +
        df["Body"].fillna("")
    )

    # TF-IDF
    tfidf = TfidfVectorizer(max_features=300)
    X_text = tfidf.fit_transform(df["text"]).toarray()
    text_features = pd.DataFrame(X_text, columns=tfidf.get_feature_names_out())

    # combine numeric features
    numeric_cols = ["ViewCount", "AnswerCount", "CommentCount"]
    for col in numeric_cols:
        if col not in df.columns:
            df[col] = 0
    X_numeric = df[numeric_cols].fillna(0)

    # combine text + numeric
    X = pd.concat([text_features, X_numeric], axis=1)

    # column 'target'
    X["target"] = df["target"]

    # save to CSV file
    X.to_csv(output_csv, index=False)
    print(f"✅ [featurize] Output saved to {output_csv}")

if __name__ == "__main__":
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    featurize(input_csv, output_csv)
