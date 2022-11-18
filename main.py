import os
from jinja2 import Environment, FileSystemLoader

max_score = os.getenv('MAX_SCORE', 100)
test_name = os.getenv('TEST_NAME', 'DevOps challenge')

# TODO: fetch API data from somewhere
players = [
    {"name": "Foo",  "score": 100},
    {"name": "Bar", "score": 87},
    {"name": "Baz", "score": 40},
    {"name": "Unknown", "score": 75},
]

def main():
    """The main function.
    """
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("message.txt")
    for player in players:
        filename = f"dist/{player['name'].lower()}.txt"
        content = template.render(
            player, 
            max_score=max_score,
            test_name=test_name,
            author="Admin"
            )
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")

if __name__ == "__main__":
    main()
