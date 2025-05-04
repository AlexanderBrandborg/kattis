def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0
    for c in input():
        if(c in vowels):
            counter += 1
    print(counter)

if __name__=="__main__":
    main()