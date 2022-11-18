from jinja2 import Environment, FileSystemLoader

players = [
    {"name": "Foo",  "score": 100},
    {"name": "Bar", "score": 87},
    {"name": "Baz", "score": 40},
    {"name": "Unknown", "score": 75},
]

test_name = "Python Challenge"
max_score = 100
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

def main():
    """The main function.
    """
    for player in players:
        filename = f"message_{player['name'].lower()}.txt"
        content = template.render(
            player, 
            max_score=max_score,
            test_name=test_name,
            author="Admin"
            )
        print(f"{content}")

if __name__ == "__main__":
    main()