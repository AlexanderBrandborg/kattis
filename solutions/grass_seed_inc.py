# Difficulty: 1.3
# Url: https://open.kattis.com/problems/grassseed
def main():
    cost = float(input())
    num_lawns = int(input())

    total = 0
    for _ in range(num_lawns):
        dimensions = input().split(" ")
        total += (float(dimensions[0]) * float(dimensions[1])) * cost

    print(total)

if __name__=="__main__":
    main()