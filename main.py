import functions
import datetime

print(f"""
TOMAS' DATABASE RECIPE TRACKER
______________________________
{datetime.date.today()}

VIEW  - view all recipes
OVIEW - ordered view of recipes
INCL  - includes ingredient
RAND  - radom meal select
ADD   - add new recipe
DEL   - delete recipe
END   - quit programme
""")

while True:
    choice = input("\n>>> ").lower()
    if choice == "view":
        functions.view_recipes()
    if choice == "oview":
        functions.ordered_view()
    if choice == "incl":
        functions.includes_ingredient()
    if choice == "rand":
        functions.random_select()
    if choice == "add":
        functions.add_recipe()
    if choice == "del":
        functions.delete_recipe()
    if choice == "end":
        break
