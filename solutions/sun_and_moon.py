# Difficulty: 2.1
# Url: https://open.kattis.com/problems/sunandmoon?tab=metadata
def main():
    line1 = input().split()
    current_sun_year = int(line1[0])
    sun_cycle_years = int(line1[1])

    line2 = input().split()
    current_moon_year = int(line2[0])
    moon_cycle_years = int(line2[1])

    for i in range(5000):
        if(current_moon_year == moon_cycle_years and current_sun_year == sun_cycle_years):
            print(i)
            break

        current_moon_year = 1 if current_moon_year == moon_cycle_years else current_moon_year + 1
        current_sun_year = 1 if current_sun_year == sun_cycle_years else current_sun_year + 1
        
if __name__=="__main__":
    main()