from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def format_date(value, fmt='%d-%m-%Y %H:%M:%S'):
    return value.strftime(fmt)


loader = FileSystemLoader(searchpath="./templates")
env = Environment(loader=loader)
env.filters["format_date"] = format_date

template = env.get_template("query.template")
sql = template.render(
    db_name="MY_DB",
    table_name="Users",
    variables=[
        {"field_name": "name", "field_type": "VARCHAR"},
        {"field_name": "age", "field_type": "INTEGER "},
        {"field_name": "timestamp", "field_type": "DATE"},
    ],
    date=datetime.now(),
    orderby=None
)
print(sql)
