import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='copy and paste your client id here',
                     client_secret='copy and paste your secret here',
                     user_agent='my user agent'
                     )

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
    return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
    return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
    return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


def main():
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    print(comments[0].body)
    print(comments[0].replies[0].body)

    neg = get_text_negative_proba(comments[0].replies[0].body)

    print(neg)


main()
