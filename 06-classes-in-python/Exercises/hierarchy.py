class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    def getname(self):
        return self.name

    def pension(self):
        return self.years * self.salary * 0.1

class Manager(Worker):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * self.salary * 0.2

class Executive(Manager):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * self.salary * 0.3

def main():
    workers = [
        Manager("Chris", 100000, 10),
        Executive("Susan", 100000, 10),
        Worker("Michael", 100000, 10)
    ]

    for idx, worker in enumerate(workers):
        print("{:3} {:15.2f} {}".format(idx, worker.pension(), worker.getname()))

if __name__ == "__main__":
    main()