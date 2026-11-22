# Q11. Build a Local News Data Viewer

# Concept: Functions and data processing

# Requirements:

    # Create a sample news dataset.
    # Display all news.
    # Search by keyword.
    # Filter by category.
    # Display total articles.

# Steps to Solve:

    # Create a list of news dictionaries.
    # Create a function to display all news.
    # Create a function to search by keyword.
    # Create a function to filter by category.
    # Create a function to count articles.
    # Build a menu using loops and 

#---------------------------------------------------------------------------------------------------------------

news_data = [
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
        "title": "Football league starts next week",
        "category": "Sports"
    }
]


def display_all_news():
    print("\nAll News Articles:\n")

    for article in news_data:
        print(f"Title    : {article['title']}")
        print(f"Category : {article['category']}")
        print("-" * 40)


def search_by_keyword():
    keyword = input("Enter keyword: ").lower()

    found = False

    for article in news_data:
        if keyword in article["title"].lower():
            print(article["title"])
            found = True

    if not found:
        print("No matching articles found.")


def filter_by_category():
    category = input("Enter category: ").lower()

    found = False

    for article in news_data:
        if article["category"].lower() == category:
            print(article["title"])
            found = True

    if not found:
        print("No articles found in this category.")


def count_articles():
    print(f"Total Articles: {len(news_data)}")


while True:

    print("\n===== NEWS DATA VIEWER =====")
    print("1. Display All News")
    print("2. Search By Keyword")
    print("3. Filter By Category")
    print("4. Total Articles")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all_news()

    elif choice == "2":
        search_by_keyword()

    elif choice == "3":
        filter_by_category()

    elif choice == "4":
        count_articles()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice.")
