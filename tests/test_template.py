import jinja2

def test_template():
    path = "templates"
    filename = "message.txt.j2"
    rendered = (
        jinja2.Environment(loader=jinja2.FileSystemLoader(path))
        .get_template(filename)
        .render(
            score=99,
            max_score=100,
            test_name="Foo",
            author="Author",
        )
    )
    assert "Author" in rendered
