import os
import json
import pandas as pd
import streamlit as st

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None

        # Build absolute path (works in local + Streamlit Cloud)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.join(base_dir, file_path)

        # If processed file missing, generate it
        if not os.path.exists(abs_path):
            st.warning("processed_posts.json missing. Generating from raw_posts.json...")
            from preprocess import process_posts
            os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)
            process_posts(
                os.path.join(base_dir, "data", "raw_posts.json"),
                os.path.join(base_dir, "data", "processed_posts.json")
            )

        self.load_posts(abs_path)

    def load_posts(self, abs_path):
        with open(abs_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain 'Influencer'
            (self.df['language'] == language) &  # Language is 'English'
            (self.df['length'] == length)  # Line count is less than 5
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    # print(fs.get_tags())
    posts = fs.get_filtered_posts("Medium","Hinglish","Job Search")

    print(posts)
