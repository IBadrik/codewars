def weather_info(temp):
    celsius = (temp - 32) * (5 / 9)
    if (celsius < 0): return str(celsius) + " is freezing temperature"
    else: return str(celsius) + " is above freezing temperature"

# In this kata I need to debug celcius converter
# def weather_info (temp):
#     c : convert(temp)
#     if (c > 0):
#         return (c + " is freezing temperature")
#     else:
#         return (c + " is above freezing temperature")
#
# def convert_to_celsius (temperature):
#   var celsius = (tempertur) - 32 + (5/9)
#   return temperature
