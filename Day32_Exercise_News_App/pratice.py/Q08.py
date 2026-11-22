# Q8. Sort News Articles

# Concept: Sorting and lambda

# Requirements:

    # Create articles with publication dates or timestamps.
    # Sort the articles.
    # Display the sorted result.

# Steps to Solve:

    # Create a list of article dictionaries.
    # Add a date field to each article.
    # Understand the date format.
    # Use sorting with an appropriate key.
    # Display articles in chronological or reverse chronological order.

#-----------------------------------------------------------------------------------------------------------------------------------------

articles = [
    {
        "title": "AI is changing education",
        "date": "2026-11-20"
    },
    {
        "title": "India wins cricket match",
        "date": "2026-11-18"
    },
    {
        "title": "New space mission launched",
        "date": "2026-11-22"
    },
    {
        "title": "Stock market reaches new high",
        "date": "2026-11-15"
    },
    {
        "title": "Heavy rainfall expected tomorrow",
        "date": "2026-11-19"
    }
]

# Chronological Order (Oldest to Newest)
sorted_articles = sorted(
    articles,
    key=lambda article: article["date"]
)

print("Chronological Order:\n")

for article in sorted_articles:
    print(f"Title: {article['title']}")
    print(f"Date : {article['date']}")
    print("-" * 40)
