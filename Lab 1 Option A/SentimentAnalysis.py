import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw
import ssl

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
    # Checks if the appropriate data types are passed.
    if not isinstance(comments, praw.models.comment_forest.CommentForest) and \
            isinstance(lists, list) and isinstance(lists[0], list) \
            and isinstance(lists[1], list) and isinstance(lists[2], list):
        return
    if not isinstance(index, int):
        return

    # Base Case.
    if comments is None:
        return
    if index >= len(comments):
        return

    # Adds to the actual list.
    process_string(comments[index].body, lists)


    process_comments(comments[index].replies, 0, lists)
    process_comments(comments, index + 1, lists)


def process_string(body, lists):
    """
    Will add given string 'body' to either negative, positive, or neutral lists based on
    the highest probability in the 'values' list.
    """
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
    Tests Case 1 is just a smaller version of the given test case.
    I'm checking that each list is being filled accordingly.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/czg123/test_case_1/')
    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)

    print("Test Case 1")
    print('Expected Negative: 3, Actual: ', len(negative_list))
    print('Expected Positive: 2, Actual: ', len(neutral_list))
    print('Expected Neutral: 2, Actual: ', len(positive_list))


def test_case_2():
    """
    Tests Case 2 tests that each nested comment is evaluated.
    It tests that each lists is being filled accordingly. Only neutral comments should
    have data.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/d21mre/neutral_comments/')
    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)
    print("Test Case 2")
    print('Expected Negative: 0, Actual: ', len(negative_list))
    print('Expected Positive: 6, Actual: ', len(neutral_list))
    print('Expected Neutral: 0, Actual: ', len(positive_list))


def test_case_3():
    """
    Tests Case 3 tests that the program does not crash if there is no comments.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/d21r2o/empty_link/')
    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)
    print("Test Case 3")
    print('Expected Negative: 0, Actual: ', len(negative_list))
    print('Expected Positive: 6, Actual: ', len(neutral_list))
    print('Expected Neutral: 0, Actual: ', len(positive_list))


def test_case_4():
    """
    Tests that the program will not fail if the user does not pass correct data types,
    the program should simply not run.
    """
    comments = get_submission_comments(
        'https://www.reddit.com/user/Edd1e234/comments/d21r2o/empty_link/')
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments("not comment", 0, lists)
    process_comments(comments, "not an index", lists)
    process_comments(comments, 0, "Not a list")

    lists[0] = "not a list"
    process_comments(comments, 0, lists)

    print("\nTest case 4 did not fail.")


def main():
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    print(comments[0].body)
    print(comments[0].replies[0].body)

    print(type(comments))

    # Output Lists.
    negative_list, positive_list, neutral_list = [], [], []
    lists = [negative_list, positive_list, neutral_list]
    process_comments(comments, 0, lists)

    print("\nGiven link")
    print('Negative comments amount: ', len(negative_list))
    print('Positive comments amount: ', len(positive_list))
    print('Neutral comments amount: ', len(neutral_list), '\n')

    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()


main()
