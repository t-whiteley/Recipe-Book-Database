
import sqlite3
from random import choice


def random_select():
    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    recipes_lst = [row[0] for row in data_in_rows]
    random_recipe = choice(recipes_lst)
    print(random_recipe)


random_select()
