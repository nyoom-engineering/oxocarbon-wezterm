import yaml
import jinja2


def read_theme(name: str):
    theme = {}

    with open(f"palette/base16-oxocarbon-{name}.yaml", "r") as f:
        theme = yaml.safe_load(f)
        f.close()

    return theme


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates/"))
    tmp = env.get_template("oxocarbon-dark.toml.j2")
    thm = read_theme('dark')

    con = tmp.render(thm)

    open('oxocarbon-dark.toml', 'w').close()

    with open('oxocarbon-dark.toml', 'w') as f:
        f.write(con)
        f.close()


main()
