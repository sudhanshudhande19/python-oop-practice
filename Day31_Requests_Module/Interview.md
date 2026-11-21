# 14. Interview Questions

1. **What is the Requests module in Python?**

    It is a Python library used to send HTTP requests and communicate with websites and APIs.

2. **How do you install Requests?**

    Run `pip install requests` in the terminal.

3. **What is an API?**

    An API is an interface that lets two software applications communicate.
    
4. **What is HTTP?**

   HTTP is the protocol used for communication between web clients and servers.

5. **What is the difference between GET and POST?**

    `GET` retrieves data; `POST` sends data to a server.

6. **What does `requests.get()` do?**

    It sends an HTTP GET request to retrieve data from a URL.

7. **What is a response object?**

    It stores the server's reply, including status, headers, and response data.

8. **What is the use of `response.status_code`?**

    It gives the HTTP status number, such as `200` or `404`.

9. **What is the difference between `response.text` and `response.json()`?**

     `text` gives the response as text; `json()` parses JSON into Python data.

10. **What is JSON?**

    JSON is a text format used to exchange data between applications.

11. **What are HTTP status codes?**

     They are numbers that describe the result of an HTTP request.

12. **What is the purpose of query parameters?**

    They send extra filtering or search information with a request URL.

13. **What is the use of `timeout`?**

    It stops a request from waiting indefinitely.

14. **What does `raise_for_status()` do?**

    It raises an HTTP error when the response status indicates failure (4xx or 5xx).

15.**How do you handle Requests exceptions?**

    Use `try-except`, commonly catching `requests.exceptions.RequestException`.

16. **What is the difference between `data` and `json` in a POST request?**

   `data` sends form/body data; `json` sends JSON-encoded data.

