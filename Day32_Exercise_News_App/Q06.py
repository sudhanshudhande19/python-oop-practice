# Q6. Filter News by Keyword

# Concept: Conditions and string methods

# Requirements:

    # Create a list of news articles.
    # Search for a keyword in article titles.
    # Display matching articles.

# Steps to Solve:

    # Create at least five article dictionaries.
    # Ask the user to enter a keyword.
    # Convert the keyword and titles to lowercase.
    # Check whether the keyword exists in each title.
    # Disilay matching headlines.
    # Display a message if no matches are found.

#-------------------------------------------------------------------------------------------------

articles = [
    {"title": "AI is changing education"},
    {"title": "India wins cricket match"},
    {"title": "New AI tools launched"},
    {"title": "Space mission successful"},
    {"title": "Technology trends in 2026"}
]

keyword = input("Enter Keyword = ").lower()

found = False

for article in articles:
    title = article["title"]

    if keyword in title.lower():
        print(title)
        found = True

if not found:
    print("No matching headlines found.")