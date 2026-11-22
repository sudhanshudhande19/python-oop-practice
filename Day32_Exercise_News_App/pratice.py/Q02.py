# Q2. Display News Headlines

# Concept: Loops and dictionary access

# Requirements:

    # Create at least five sample news articles.
    # Display every headline.
    # Display the article number.

# Steps to Solve:

    # Create a list of article dictionaries.
    # Add a title to each dictionary.
    # Use a loop to access the articles.
    # Display the title.
    # Use a counter or enumerate() to display article numbers.

#----------------------------------------------------------------------------------------------------------------------------



news_response = {
    'Articles' : [
        {
            'title' : 'AI chnages Education',
            'description' : 'AI is transformating learing',
        } ,
        {
            'title' : 'Cricket world Cup',
            'decsription' : 'India won the match'
        },
        {
            'title' : 'AI chnages Education',
            'description' : 'AI is transformating learing',
        } ,
        {
            'title' : 'Cricket world Cup',
            'decsription' : 'India won the match'
        },
        {
            'title' : 'Cricket world Cup',
            'decsription' : 'India won the match'
        },
                
        
    ]
}
count  = 1
for article in news_response['Articles']:
    print('Articles',count,'=', article['title'])
    count += 1

print('-----------------------------------------')

for number, article in enumerate(news_response["Articles"], start=1):
    print(f"Article {number}: {article['title']}")