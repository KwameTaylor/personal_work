# fizzbuzz time!
# kwame taylor

def run_fizzbuzz(i):
    for i in range(1, i+1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

i = 100
run_fizzbuzz(i)