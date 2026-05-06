class Car:
    def __init__(self, model, year, color, for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.forsale=for_sale

    def drive(self):
        print(f"You are driving {self.color} {self.model}.")

    def stop(self):
        print(f"You are stopped {self.color} {self.model}.")

    def describe(self):
        print(f"{self.color} {self.model} {self.year} model, {'available' if self.forsale else 'not available'} right now")