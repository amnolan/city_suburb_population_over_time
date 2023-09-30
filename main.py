# Population system between city and subburb: City-dwellers moving to burbs and burb-dwellers moving to city
# finds the population after N years.
#
# I find linear algebra pretty tedious and mind-numbing. It is so easy to make a mistake, so it's good to have a way to check your work quickly.
# This is a matrix problem, but I didn't feel it was necessary to use matricies for a 2x2 * 2x1 matrix.
# The program takes in the population leaving the city and the population leaving the subburb and figures out the difference.
# Then it applies matrix multiplication to tell what the population will be in N years.
#
print("city, suburb population over time")
print("enter pop leaving city as integer representing %: ")
leaving_city = float(input())
print("enter pop leaving subburb as integer representing %: ")
leaving_burb = float(input())
print("enter city population as integer: ")
city_pop = int(input())
print("enter subburb population as integer: ")
burb_pop = int(input())
print("how many years in the future: ")
years_future = int(input())
staying_city = round(1 - leaving_city,2)
staying_burb = round(1 - leaving_burb,2)

print(staying_city)
print(staying_burb)

# feed the city and suburb population back in
for i in range(years_future):
    city_res = (staying_city * city_pop)+(leaving_burb * burb_pop)
    burb_res = (leaving_city * city_pop)+(staying_burb*burb_pop)
    print(city_res)
    print(burb_res)
    city_pop = int(city_res)
    burb_pop = int(burb_res)
    
