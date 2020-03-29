import zipfile

import requests
from chalice import Chalice
import os

GITHUB_ZIP_URL = 'https://github.com/owenbrown/ashitaka/archive/master.zip'

app = Chalice(app_name='eboshi')


@app.route('/')
def index():
    print("index hit")
    return {'hello': 'world'}


@app.route('/push', methods=['GET', 'POST'])
def push():
    print("/push route hit")
    res = requests.get(GITHUB_ZIP_URL)
    open('data.zip', 'wb').write(res.content)
    print("The request was successful.")
    z = zipfile.Zipfile(file='data.zip')
    return {'hello': 'world'}


if __name__ == '__main__':
    try:
        os.makedirs("repo")
    except FileExistsError:
        # directory already exists
        pass
    res = requests.get(GITHUB_ZIP_URL, allow_redirects=True)
    print(res)
    print(res.headers)
    open('repo/zipfile.zip', 'wb').write(res.content)
    zipfile.ZipFile(file='repo/zipfile.zip').extractall('repo')


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
