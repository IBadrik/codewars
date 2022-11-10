def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'

# In this kata You're writing code to control your town's traffic lights.
# You need a function to handle each change from green, to yellow, to red, and then to green again.