#Calcula sequencia fibonacci
def fibonacci():
        fim = int(input("\nDigite a quantidade de números Fibonacci:"))
        while fim <1:
            fim = int(input("\nDigite a quantidade de números Fibonacci:"))

        f1 = 0
        f2 = 1

        print("\nSequência Fibonacci:")
        print("________________________________________")
        print("1   |phi= 1.000|  ", end="")

        for i in range(0,fim-1,1):

            f3 = f1+f2
            f1 = f2
            f2 = f3
            phi = f2/f1

            print(f3, '  |phi= %.3f|  ' %phi, end=" ")
        print("\n")

if __name__ == "__main__":
    fibonacci()