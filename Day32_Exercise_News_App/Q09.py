# Q9. Handle Empty News Results

# Concept: Conditions and error handling

# Requirements:

    # Create an empty articles list.
    # Check whether articles are available.
    # Display an appropriate message.

# Steps to Solve:

    # Create an empty list.
    # Check whether the list contains data.
    # Display a message when it is empty.
    # Add sample articles.
    # Test the program again with available data.


#--------------------------------------------------------------------------------------------------------------



articles = []


if articles:
    print("News Articles Found:")
    for article in articles:
        print(article["title"])
else:
    print("No news articles available.")

articles = [
    {"title": "AI is changing education"},
    {"title": "India wins cricket match"},
    {"title": "New space mission launched"}
]


if articles:
    print("News Articles Found:")

    for article in articles:
        print(article["title"])
else:
    print("No news articles available.")