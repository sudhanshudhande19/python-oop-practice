#  Interview Questions

**1. What is a News API?**  
A News API is an online service that provides news data to applications.

**2. How does a Python News App work?**  
Python requests news from an API, reads the JSON response, and displays article details.

**3. What is the purpose of the Requests library?**  
It helps Python send HTTP requests and receive data from websites and APIs.

**4. What is the difference between an API endpoint and a URL?**  
A URL is any web address; an endpoint is a URL used to access a particular API resource.

**5. What is JSON response processing?**  
It means converting the API's JSON response into Python data and using its values.

**6. How do you extract articles from an API response?**  
Use `data.get("articles", [])` to get the article list, then loop through it.

**7. What is the purpose of query parameters?**  
They pass extra options, such as a search keyword, country, or category, to the API.

**8. Why do some APIs require API keys?**  
An API key identifies the user or application and helps control access and usage.

**9. How do you protect an API key?**  
Store it in an environment variable or `.env` file and never commit it to GitHub.

**10. How do you handle missing article descriptions?**  
Use `.get()` with a default message, such as `article.get("description") or "Not available"`.

**11. What is the purpose of `response.raise_for_status()`?**  
It raises an HTTP error when the response has an unsuccessful status code.

**12. How do you handle API timeout errors?**  
Set a timeout in the request and catch `requests.exceptions.Timeout` using `try-except`.

**13. What is the difference between an empty response and a failed request?**  
An empty result means the request worked but found no articles; a failed request means the API call itself did not succeed.

**14. How can you search news by keyword?**  
Send the keyword as a query parameter, or compare it with article titles in the returned data.

**15. How can you filter news by category?**  
Pass a category parameter if the API supports it, then display the matching articles.

> **Quick revision:** API gives news, Requests fetches it, JSON carries it, Python extracts it, and exception handling manages errors.
