"""Reusable experiment functions extracted from index.ipynb."""

from __future__ import annotations


def load_files_and_split_articles(directory):
    import os
    import re

    all_articles = []
    if not os.path.exists(directory):
        raise ValueError(f"Directory {directory} does not exist.")
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read().lower()
                    articles = re.split("document\\s+\\w{25}", text)
                    articles = [article.strip() for article in articles if article.strip() != ""]
                    all_articles.extend(articles)
            except (OSError, UnicodeError) as exc:
                raise ValueError(f"Could not read article file: {filename}") from exc
    return all_articles


def separate_metadata(article):
    import re

    end_of_metadata_pattern = re.compile(
        "All Rights Reserved\\.|Copyright \\d{4}\\. Dow Jones & Company, Inc\\.",
        re.IGNORECASE,
    )
    match = end_of_metadata_pattern.search(article)
    if match:
        end_of_metadata_index = match.end()
        metadata = article[:end_of_metadata_index].strip()
        content = article[end_of_metadata_index:].strip()
        return (metadata, content)
    else:
        return ("", article)


def remove_punctuation(article):
    import re

    punctuation_pattern = "[!\"#$%&\\'()*+,\\-./:;<=>?@\\[\\\\\\]^_`{|}~\\n]+"
    return re.sub(punctuation_pattern, " ", article)


def remove_stop_words_and_convert_numbers(article, stop_words):
    from nltk.tokenize import word_tokenize
    from num2words import num2words

    words = word_tokenize(article)
    new_text = []
    for w in words:
        if w.lower() not in stop_words and len(w) > 1:
            try:
                w = num2words(int(w))
            except ValueError:
                pass
            new_text.append(w)
    return " ".join(new_text).lower().replace("-", " ")
