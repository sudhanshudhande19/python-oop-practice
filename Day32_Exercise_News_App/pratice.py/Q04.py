# Q4. Display News Source and Author

# Concept: Nested dictionaries

# Requirements:

    # Store news source information.
    # Store the author's name.
    # Display the source and author.

# Steps to Solve:

    # Create an article dictionary.
    # Add a nested source dictionary.
    # Store the source name.
    # Store the author's name.
    # Access the nested dictionary.
    # Handle missing author or source information.

#------------------------------------------------------------------------------------------------


news_response = {
    'Articles' : [
        {
         
            'author' : 'sudhanshu',
            'source' : {
                'name' : 'BBC News'
            }
        } ,
        {
      
            'author' : 'Joy',
            'source' : {
                'name' : "ABP News"
            }
        },
        {
            
            'author' : 'kunal',
            'source' : {
                'name' : 'India News'
            }
        } ,
        {
          
            'author' : 'jack',
            'source' : {
                'name' : ''
            }
        },
        {
            'author' : '',
            'source' : {
                'name' : 'All Time News'
            }
        },
                   
    ]
}

if news_response:
    for article in news_response['Articles']:

        author = article.get('author') or 'Author unavailable'
        source = article.get('source',{}).get('name') or 'source Unavailable'

        print(f'Author = {author}')
        print(f'Source = {source}')
        print('---------------------')
else:
    print('not found')