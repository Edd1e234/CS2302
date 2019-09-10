import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw
import ssl

# Lists

# Setup
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
reddit = praw.Reddit(client_id='mSLWtJwBCM7QeQ',
                     client_secret='1mPjfETG1EA-wKfL2DxYBo4ndbQ',
                     user_agent='Edd1e234'
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


def process_comments(comments, index, lists):
    # Base Case.
    if comments is None:
        return
    if index >= len(comments):
        return

    process_string(comments[index].body, lists)
    process_comments(comments[index].replies, 0, lists)
    process_comments(comments, index + 1, lists)


def process_string(body, lists):
    # Mapped the same as the lists index's.
    values = [get_text_negative_proba(body),
              get_text_positive_proba(body),
              get_text_neutral_proba(body)]

    max_value = 0.0
    index = 0

    # Finds the highest value.
    for i in range(3):
        if max_value <= values[i]:
            # Index is saved.
            index = i
            max_value = values[i]

    lists[index].append(body)


def test_case_1():
    """
    Tests Case 1 tests that each comment is evaluated.
    It tests that each lists is being filled accordingly.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/czg123/test_case_1/')
    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)

    print("Test Case 1")
    print('Expected: 3, Actual: ', len(negative_list))
    print('Expected: 2, Actual: ', len(neutral_list))
    print('Expected: 2, Actual: ', len(positive_list))


def test_case_2():
    """
    Tests Case 1 tests that each comment is evaluated.
    It tests that each lists is being filled accordingly.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/czg123/test_case_1/')
    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)



def main():
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    print(comments[0].body)
    print(comments[0].replies[0].body)

    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)

    print("\nGiven link")
    print('Negative comments amount: ', len(negative_list))
    print('Positive comments amount: ', len(positive_list))
    print('Neutral comments amount: ', len(neutral_list), '\n')

    test_case_1()


main()
