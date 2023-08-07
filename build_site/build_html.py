from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("_templates/"))

template = environment.get_template("index.j2")

output = template.render(*vars)

with open("_site/index.html", "wt") as index_file:
    index_file.write(output)


