# Q7. Search News by Category

# Concept: Filtering data

# Requirements:

    # Create news articles with categories.
    # Allow the user to enter a category.
    # Display articles belonging to that category.

# Steps to Solve:

    # Create article dictionaries with title and category.
    # Ask the user to enter a category.
    # Compare the entered category with article categories.
    # Display matching articles.
    # Handle categories with no matching results.


#--------------------------------------------------------------------------------------------------
import requests

articles = [
    {
        "title": "AI is changing education",
        "category": "Technology"
    },
    {
        "title": "India wins cricket match",
        "category": "Sports"
    },
    {
        "title": "New space mission launched",
        "category": "Science"
    },
    {
        "title": "Stock market reaches new high",
        "category": "Business"
    },
    {
        "title": "Heavy rainfall expected tomorrow",
        "category": "Weather"
    }
]

user = input('Enter The Category =')

found = False

for cat in articles:
    if cat['category'] == user:
        print(f'{cat['category']} is matching')
        found = True

if not found:
    print('No Matching category')