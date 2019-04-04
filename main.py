# Employee class is the blueprint for all objects created using it
class Employee:
    # this is a class variable, shared by all instances. The base employee raise is 4%
    wage_raise = 1.04

    # this is the constructor which is ran upon a new object being created
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    # this is our add_raise method which takes the employees current wage and increases it by the base wage
    def add_raise(self):
        self.wage = self.wage*self.wage_raise


def main():
    # creating a jeffrey employee and setting jeffrey's wage to 45000
    jeffrey = Employee("Jeffrey", 45000)
    print(jeffrey.wage)
    jeffrey.add_raise()
    print("Jeff's Wage: " + str(jeffrey.wage))


# this is the way for the interpreter to see if this script is being ran directly or being used by another program.
if __name__ == "__main__":
    main()
