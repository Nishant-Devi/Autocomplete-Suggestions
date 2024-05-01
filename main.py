import json
import requests
from fake_useragent import UserAgent

user_agent = UserAgent()

completion_query = 'Nvidia'

# Generate a random User-Agent string
random_user_agent = user_agent.random

# Set the user agent header
headers = {'User-Agent': random_user_agent}

response = requests.get(f'http://google.com/complete/search?client=chrome&q={completion_query}', headers= headers)

"""print(json.loads(response.text)[1]):
 This converts the JSON-formatted text content of the response into a Python object.
 The json.loads() function is used to deserialize the JSON string (converting a JSON-formatted string
 into a native Python data structure, typically a dictionary, list, string, integer, float, boolean, or None.).
 After this operation, we have a Python object that corresponds to the JSON data.
 [1]: This indexing operation selects the second element of the Python object obtained from deserializing the JSON data."""

for completion in json.loads(response.text)[1]:
    print(completion)