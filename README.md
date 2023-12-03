Flask is a lightweight Python web framework that provides useful tools and features for creating web applications in the Python Language.

When developing a web application, it is important to separate **business logic** from presentation logic. Business logic is what handles user requests and talks to the database to build an appropriate response. Presentation logic is how the data is presented to the user, typically using HTML files to build the basic structure of the response web page, and CSS styles to style HTML components. For example, in a social media application, you might have a username field and a password field that can be displayed only when the user is not logged in. If the user is logged in, you display a logout button instead. This is the **presentation logic**. If a user types in their username and password, you can use Flask to perform business logic: You extract the data (the username and password) from the request, log the user in if the credentials are correct or respond with an error message. How the error message is displayed will be handled by the presentation logic.


In Flask, you can use the Jinja templating language to render HTML templates. A template is a file that can contain both fixed and dynamic content. 

 When a user requests something from your application (such as an index page, or a login page), Jinja allows you to respond with an HTML template where you can use many features that are not available in standard HTML, such as variables, if statements, for loops, filters, and template inheritance.

## Install packages

Install related python packages
`pip install flask`

`pip install flask-login`

Allows us to create SQL database models
`pip install flask-sqlalchemy`

## __init__.py

When we place it inside a folder, the folder becomes a Python package. 

Can import the folder and we
```
```

A **route **is a URL you can use to determine what the user receives when they visit your web application on their browser. For example, http://127.0.0.1:5000/ is the main route that might be used to display an index page.

## main.py

we will import website package and use it create an application and run run it

``` if __name__ == '__main__': ```
Stipulates that only runs the website isf we run the file directly

`    app.run(debug=True)`

Makes sure that anytime we make changes to the code it automatically reruns/updates the web server(SHOULD BE OFF IN PRODUCTION)

## views.py

This is the website roopt. i.r
The pages for the website e.g Aboput page

#POST requests
when we send this form, send a POST request to the backend


## RESOURCES
1. (https://www.youtube.com/watch?v=dam0GPOAvVI)
2. (https://pythonprogramming.net/password-hashing-flask-tutorial/)
3. (https://www.programcreek.com/python/example/97491/passlib.hash.sha256_crypt.verify)

