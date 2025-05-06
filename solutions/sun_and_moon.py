# Difficulty: 2.1
# Url: https://open.kattis.com/problems/sunandmoon?tab=metadata
def main():
    line1 = input().split()
    current_sun_year = int(line1[0])
    years_in_sun_cycle = int(line1[1])

    line2 = input().split()
    current_moon_year = int(line2[0])
    years_in_moon_cycle = int(line2[1])

    for i in range(5000):
        if(current_moon_year == years_in_moon_cycle and current_sun_year == years_in_sun_cycle):
            print(i)
            break

        current_moon_year = 1 if current_moon_year == years_in_moon_cycle else current_moon_year + 1
        current_sun_year = 1 if current_sun_year == years_in_sun_cycle else current_sun_year + 1
       
if __name__=="__main__":
    main()