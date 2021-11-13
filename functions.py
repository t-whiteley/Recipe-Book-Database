import sqlite3
from random import choice


def add_recipe():
    new_recipe = {
        "name": input("name: "),
        "time": int(input("time: ")),
        "ingredients": input("ingredients: ")
    }

    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        command = "INSERT INTO Recipes VALUES(?, ?, ?)"
        connection.execute(command, tuple(new_recipe.values()))
        print("*add succesful")
    connection.commit()


def view_recipes():
    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    print("name - time - ingredients.")
    for row in data_in_rows:
        print(f"\n{row[0].upper()} - {row[1]} mins - [{row[2]}]")


def ordered_view():
    orderby = input("(APLPHA) or (TIME): ").lower()
    sorter = "name"
    if orderby == "alpha":
        sorter = "name"
    elif orderby == "time":
        sorter = "time"

    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        command = f"SELECT * FROM Recipes ORDER BY {sorter} ASC"
        cur = connection.cursor()
        cur.execute(command)
    connection.commit()

    data_in_rows = cur.fetchall()
    print("name - time - ingredients.")
    for row in data_in_rows:
        print(f"\n{row[0].upper()} - {row[1]} mins - [{row[2]}]")


def delete_recipe():
    selected_name = str(input("name: ")).lower()

    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        command = "DELETE from Recipes WHERE name = ?"
        cur = connection.cursor()
        cur.execute(command, (selected_name,))
        print("*delete succesful")
    connection.commit()


def includes_ingredient():
    ingredient = str(input("ingredient: "))

    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    print("name - time - ingredients.")
    for row in data_in_rows:
        if ingredient in row[2]:
            print(f"\n{row[0].upper()} - {row[1]} mins - [{row[2]}]")


def random_select():
    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    recipes_lst = [row[0] for row in data_in_rows]
    random_recipe = choice(recipes_lst)
    print(random_recipe)


def get_list_recipe():
    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    recipes_lst = [row for row in data_in_rows]
    return recipes_lst


def get_random():
    with sqlite3.connect("recipe_dp.sqlite3") as connection:
        cur = connection.cursor()
        command = "SELECT * FROM Recipes"
        cur.execute(command)
    data_in_rows = cur.fetchall()

    recipes_lst = [row[0] for row in data_in_rows]
    random_recipe = choice(recipes_lst)
    return random_recipe
