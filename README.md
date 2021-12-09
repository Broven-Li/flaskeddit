# flaskeddit


A simplified Reddit clone built with Flask.


## Features

- Registration and authentication.
- Create communities.
- Create community posts.
- Reply to community posts.
- Edit or delete your communities, posts, and replies.
- Join communities.
- Get a feed of posts from your joined communities.
- Upvote or downvote posts and replies.
- Sort communities, posts, and replies by latest or most popular.
- Basic user profiles.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. See deployment for notes on how to deploy the project.

### Prerequisites

To run this application you need [Python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/), and [SQLite](https://www.sqlite.org/).

### Local Setup

Clone the project.

```sh
git clone https://github.com/Broven-Li/flaskeddit.git
```

Set the `FLASK_APP` environment variable, create the SQLite database, and start the app. Now you can give the application a try at [http://localhost:5000](http://localhost:5000)!

```sh
export FLASK_APP=flaskeddit.py (set for Windows)
flask cli create_db
flask run
```

You can also serve the application locally using [gunicorn](https://gunicorn.org/).

```sh
gunicorn "flaskeddit:create_app()"
```

## Testing

Flaskeddit is tested using pytest.

Use `pytest` to run the application's tests.

```sh
pytest
```

## Contributing

Feel free to submit a pull request!

## Authors

- **Broven-Li** - _Author_ - [Broven-Li](https://github.com/Broven-Li)
