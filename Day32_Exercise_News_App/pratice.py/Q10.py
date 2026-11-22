# Q10. Create a News Summary

# Concept: String formatting and loops

# Requirements:

    # Store five news articles.
    # Display title, source, and description.
    # Format the output clearly.

# Steps to Solve:

    # Create article dictionaries.
    # Store title, source, and description.
    # Use a loop to process the articles.
    # Format each article using headings or separators.
    # Display all articles in a readable format.

#-----------------------------------------------------------------------------------------------


articles = [
    {
        "title": "AI is changing education",
        "source": "BBC News",
        "description": "AI is transforming modern learning systems."
    },
    {
        "title": "India wins cricket match",
        "source": "ESPN Cricinfo",
        "description": "India secured a thrilling victory."
    },
    {
        "title": "New space mission launched",
        "source": "NASA News",
        "description": "A new rocket was successfully launched."
    },
    {
        "title": "Stock market reaches new high",
        "source": "Economic Times",
        "description": "Markets closed at a record level today."
    },
    {
        "title": "Heavy rainfall expected tomorrow",
        "source": "Weather Channel",
        "description": "Meteorologists predict heavy rain in several regions."
    }
]

for number, article in enumerate(articles, start=1):
    print("=" * 50)
    print(f"ARTICLE {number}")
    print("=" * 50)

    print(f"Title       : {article.get('title', 'Title unavailable')}")
    print(f"Source      : {article.get('source', 'Source unavailable')}")
    print(f"Description : {article.get('description', 'Description unavailable')}")

    print()