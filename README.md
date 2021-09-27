# Python 003 - Control Flow, Logical Operators, if/elif/else

## if elif else

**If** statements can be used just like in JavaScript to set conditions for our code. We can also use **elif** as an _else if_ condition, and **else** as a final _else_ condition.

For example:

    num = 2
    if num == 1:
    	name = "Dean"
    elif num == 2:
    	name = "Matt"
    else:
    	name = "Alex"
    print(name)

Will always result in

    Matt

As that name falls under the **elif num == 2** condition.

**Note: the condition for if/elif/else is indented, key in Python. Just like in JavaScript curly braces/brackets would be used, indenting shows scope too.**

## Nested if/elif/else statements

Just like in JavaScript, if/elif/else statements can be nested to show multiple branching possibilities.

For example:

    car = input("What colour is the car, red, blue or yellow?")

    gender = input("Is the driver male or female?")

    if  car == "blue":
        if  gender == "male":
            print("The driver must be Dean.")
        else:
            print("The driver must be Ellie.")
    elif  car == "red":
        if  gender == "male":
            print("The driver must be Matt.")
        else:
            print("The driver must be Carolina.")
    else:
        if  gender == "male":
            print("The driver must be Alex.")
        else:
            print("The driver must be Kirsty.")

If the colour passed in was yellow and the gender as female, the driver would be **Kirsty**.

## Conditional Operators

      > Greater than
      < Less than
      >= Greater than or equal to
      <= Less than or equal to
      == Equal to
      != Not equal to
