munsters_description = "the Munsters are CREEPY and Spooky."
munsters_array = munsters_description.lower().split(" ")
munsters_array[0] = munsters_array[0].title()
print(' '.join(munsters_array))

# => 'The munsters are creepy and spooky.'

