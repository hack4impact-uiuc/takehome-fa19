# The Challenge

![Hack4Impact](https://uiuc.hack4impact.org/static/images/colored-logo.png)

This challenge is intended to expose you to some elements of our most common technical stack: a [React](https://reactjs.org/) frontend, and a Flask backend.

In terms of React resources, the following may be helpful:

[The React Beginner's Guide](https://flaviocopes.com/react-beginners-guide/) and [The Beginner's Guide to React](https://egghead.io/courses/the-beginner-s-guide-to-reactjs) will be very beneficial to go through to get a complete understanding on React fundamentals. It will also beneficial to get comfortable diving into [React Docs](https://reactjs.org/docs/hello-world.html) and [Javascript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) as part of this exercise.

Reading the following will help you get a sense of the big picture when it comes to developing APIs/writing server side code, and how it fits in the context of a larger web application:

- [How the Web Works](https://medium.freecodecamp.org/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c) - Read all 3 parts, especially part 3!
- [Basics of HTTP](https://egghead.io/courses/understand-the-basics-of-http)

This project will be broken down into multiple parts. After you finish this project, you must submit it by following the instructions below.

*This exercise is due before this Sunday, September 15th at 11:59PM. If you have spent over 10 hours total, submit what you have!*

For any questions, feel free to email rchiu@hack4impact.org or angad@hack4impact.org.

## Setup

First, fork this repository. The fork button on your top right. What this does is copies this repository over to your account. Now you should have a repository with the name `<yourusername>/takehome-fa19`.

Then, clone this repository (click the green button saying "Clone or Download", choose http, and copy and paste it the location `<url>` ) and go into it:

```
$ git clone <url>
$ cd takehome-fa19
```

Now open a second terminal and navigate to this cloned repository. 
In one of the terminals, run `cd backend` then follow the [backend instructions](backend/README.md).
In the other, run `cd frontend` then follow the [frontend instructions](frontend/README.md).

Postman will be useful for testing your backend as you go, you can install [here](https://www.getpostman.com/) and you will find instructions on how to use it to test the endpoints. Note that the Postman examples are about a different scenario, but they should help you to use it.

# Exercise 

The following exercise will have you learn and apply some React and Flask to build a tool to keep track of the people that you've met through making contacts.

## Flask

### Part 1 - Already Done

```
GET /contacts
```

This should return a properly formatted JSON response that contains a list of all the `contacts` in the mockdb. If you call this endpoint immediately after starting the server, you should get this response in Postman:

```
{
  "code": 200,
  "message": "",
  "result": {
      "contacts": [
          {
              "hobby": "dirty-ing",
              "id": 1,
              "name": "Angad",
              "nickname": "greg"
          },
          {
              "hobby": "weeb",
              "id": 2,
              "name": "Roy",
              "nickname": "uwu"
          },
          {
              "hobby": "losing money with options trading",
              "id": 3,
              "name": "Daniel",
              "nickname": "oppa"
          }
      ]
  },
  "success": true
}
```

### Part 2

Define the endpoint:

```
GET /contacts/<id>
```

This should retrieve a single contact that has the `id` provided from the request. For example, `GET /contacts/1` would return:

```
{
  "code": 200,
  "message": "",
  "result": {
      "hobby": "dirty-ing",
      "id": 1,
      "name": "Angad",
      "nickname": "greg"
  },
  "success": true
}
```

If there doesn't exist a show with the provided `id`, return a `404` with a descriptive `message`.

*Use Part 6, which has been completed for you, to figure out how to write this endpoint*

## Part 3

Extend the first `/contacts` enpoint by adding the ability to query contacts based on their hobby. You should _not_ use a url parameter like you did in Part 2. Instead, use a [query string](https://en.wikipedia.org/wiki/Query_string).

If `hobby` is provided as a query string parameter, only return the contacts which have that same hobby. If there are no such contacts, return a `404` with a descriptive `message`.

For this exercise, you can ignore any query string parameters other than `hobby` and you may assume that the provided parameter will be a string.

In Postman, you can supply query string parameters writing the query string into your request url or by hitting the `Params` button next to `Send`. Doing so will automatically fill in the request url.

The following should happen

```
GET /contacts?hobby=weeb

{
  "code": 200,
  "message": "",
  "result": {
      "contacts": [
          {
              "hobby": "weeb",
              "id": 2,
              "name": "Roy",
              "nickname": "uwu"
          }
      ]
  },
  "success": true
}
```

![Postman Query String Request](backend/docs/postman_querystring.png)

## Part 4

Define the endpoint:

```
POST /contacts
```

This endpoint should create a new contact. Each request should also send a `name`, `nickname`, and `hobby` parameter in the request's `body`. The `id` property will be created automatically in the mockdb.

A successful request should return a status code of `201` and return the newly created show (in the same format as Part 2).

If any of the required parameters aren't provided, DO NOT create a new show in the db and return a `422` with a useful `message`. In general, your messages should provide the user/developer useful feedback on what they did wrong and how they can fix it.

This is how you can send `body` parameters from Postman. Make sure you don't mistake this for query parameters!
![Postman POST](backend/docs/postman_post.png)

## Part 5

Define the endpoint:

```
PUT /contacts/<id>
```

Here we need to provide a contact's `id` since we need to specify which contact to update. The `body` for this request should contain the same attributes as the `POST` request from Part 4.

However, the difference with this `PUT` request is that only values with the provided keys (`name`, `hobby`) will be updated, and any parameters not provided will not change the corresponding attribute in the contact being updated.

You do not need to account for `body` parameters provided that aren't `name`, or `hobby`.

If the contact with the provided `id` cannot be found, return a `404` and a useful `message`.

If you do find the contact, return it in the same way you did in Part 4 with the updated values.

## Part 6 - Already Done

Define the endpoint:

```
DELETE /contacts/<id>
```

This will delete the contact with the associated `id`. Return a useful `message`, although nothing needs to be specified in the response's `result`.

If the contact with the provided `id` cannot be found, return a `404` and a useful `message`.

## React

### Part 1

Goal: Get familiar with JSX syntax, component structure, and passing props

Tasks:
* Send a `complete` prop into the `Instructions` component that determines whether or not to display a second line of text [Hint](https://reactjs.org/docs/conditional-rendering.html)

### Part 2
Goal: Get familiar with component state

Tasks:
* Open the empty `Counter` component file
* Set its initial state of `count` to `0`
* Display the value of the current count
* Create two buttons, one that increments the count and one that decrements it. [Hint](https://egghead.io/lessons/react-use-component-state-with-react)

### Part 3
Goal: Use nested components and props.

Tasks:
* Open the empty `Contact` component which takes a contact's `id`, `name`, `nickname`, and `hobby`.
* Display the Contact name
* To check that this works, just look at your running app, you should see 3 contacts.

### Part 4 - Already Done
Goal: Get familiar with rendering lists and javascript array functions

Tasks:
* In the `App` component, create an initial state with a list of contacts where each contact has a name, nickname, and a hobby. Use this [data](backend/mockdb/dummy_data.py)
* Display each contact by passing each contacts's attributes as props to a `Contact` component
* Do this without using `for` or `while` loops
* Very useful videos to watch:
 * [Functional Programming Intro](https://www.youtube.com/watch?v=BMUiFMZr7vk&index=1&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84) - just the first two videos are enough, although there's a lot to learn from the rest of the playlist and his other videos! (highly recommend subscribing)
 * [Rendering lists in React](https://egghead.io/lessons/egghead-use-the-key-prop-when-rendering-a-list-with-react)

### Part 5 
Goal: Get familiar with user input

Tasks:
* In `App.js`, make an input and a submit button that adds a new contact to the state (set the new contact's `id` to the next integer, and you can be creative with the remaining fields. Adding a new contact should also increment the counter.
* Note: If your button refreshes the whole page, throw in a button type: `<button type="button" ...`
