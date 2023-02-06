import json
import facebook

ACCESS_TOKEN = 'EABRlxXxMayA0BAEjeTxPEnO8FSBC60TAG694wZBy6VjwUJJ8oGh5jfcsk2PseuSH4KjS9eURa2MmqVWqTQdoLgmdxYCyKMDFJGLaNKFpAX8pfU5lD75nhVLyOQ6KY3eGNSeRl4G52UZABd6ijMmwzqZCMKzzBbUS9tEAxZATtW0FAZCIFRPqY0ZBwYF3NQ3L4SP5123scX8EWKKs78FOyaoMYyhnZBPLRRYUZA0ZCZA7YnwcS8ofgUVwtAo'

def main():
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='first_name, location, email, posts')

    print("Printing profile: ")
    print(type(profile))
    print(json.dumps(profile, indent=4))
    print(type(json.dumps(profile, indent=4)))

main()