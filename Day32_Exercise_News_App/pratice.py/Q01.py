# Q1. Understand a News JSON Response

# Concept: Dictionary and list

# Requirements:

    # Create a sample news response dictionary.
    # Store two news articles inside the articles list.
    # Display the total number of articles.

# Steps to Solve:

    # Create a dictionary containing a key named articles.
    # Store two article dictionaries inside it.
    # Add a title and description to each article.
    # Access the articles list.
    # Use len() to calculate the number of articles.
    # Display the total.

#-------------------------------------------------------------------------------------------------------------


news_response = {
    'Articles' : [
        {
            'title' : 'AI chnages Education',
            'description' : 'AI is transformating learing',
        } ,
        {
            'title' : 'Cricket world Cup',
            'decsription' : 'India won the match'
        }
    ]
}

article = news_response['Articles']

total_articles = len(article)

print('Total Articles =',total_articles)