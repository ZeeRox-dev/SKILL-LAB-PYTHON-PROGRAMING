def clean_data(user_feedback : str)->list:
    """ This function takes the user input, splits it removes any punctuation, convert all to lower case """
    return    [word.lower().strip("',.!?") for word in user_feedback.split()]

def sentiment_analysis(tokenised_list: list)-> bool:
    """ This function takes a list of tokenised words, compares each word with built-in data and returns the sentiment in the form of a boolean if negative sentiment is better than positive sentiment the bool return will be false if positive sentiment is better than negative sentiment the bool return will be true"""
    sentiment = 0
    for token in tokenised_list:
        match token:
            case "bad":
                sentiment -= 1
            case "worst":
                sentiment -= 3
            case "good":
                sentiment += 1
            case "awesome":
                sentiment += 3
            case "fantastic":
                sentiment += 3
            case "favorite":
                sentiment +=3

    if sentiment > 0:
        return True
    return False
