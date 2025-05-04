# Difficulty: 1.5
# Url: https://open.kattis.com/problems/licensetolaunch
def main():
    num_days = int(input())
    days  = input().split(" ")

    least_day_index = 0
    least_day_value = int(days[0])

    for index in range(num_days):
        day_value = int(days[index])
        if(day_value < least_day_value):
            least_day_value = day_value
            least_day_index = index
    
    print(least_day_index)

if __name__=="__main__":
    main()