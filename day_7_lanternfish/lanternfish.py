import datetime
from dataclasses import dataclass, field
from collections import deque
from multiprocessing import Queue, Pool
import threading


def main():
    do_part_1()
    do_part_2()


def do_part_1():
    print('EXAMPLE 18 DAYS')
    example = LanternfishSim(loader=Loader('example_input'), hatchery=Hatchery(), days_to_simulate=18,
                             print_output=True, day_timer=False)
    example.start()

    print('EXAMPLE 80 DAYS')
    example = LanternfishSim(loader=Loader('example_input'), hatchery=Hatchery(), days_to_simulate=80,
                             print_output=False, day_timer=False)
    example.start()

    print('USER INPUT 80 DAYS')
    app = LanternfishSim(loader=Loader('input'), hatchery=Hatchery(), days_to_simulate=80, print_output=False,
                         day_timer=False)
    app.start()


def do_part_2():
    print('EXAMPLE 18 DAYS')
    example = LanternfishSim2(loader=Loader('example_input'), days_to_simulate=18)
    example.start()

    print('EXAMPLE 80 DAYS')
    example = LanternfishSim2(loader=Loader('example_input'), days_to_simulate=80)
    example.start()

    print('EXAMPLE 256 DAYS')
    example = LanternfishSim2(loader=Loader('example_input'), days_to_simulate=256)
    example.start()

    print('USER DATA 256 DAYS')
    example = LanternfishSim2(loader=Loader('input'), days_to_simulate=256)
    example.start()


@dataclass
class Loader:
    file: str

    def get_input(self):
        with open(self.file, 'r') as f_in:
            return f_in.read()


@dataclass
class Hatchery:
    stock: list = field(default_factory=list)

    def make_baby(self, initial_timer=9):
        self.stock.append(Fish(initial_timer, self))

    def count_fish(self):
        return len(self.stock)


@dataclass
class Fish:
    internal_timer: int
    womb: Hatchery

    def age_one_day(self):
        self.internal_timer -= 1
        self.check_timer()

    def check_timer(self):
        if self.internal_timer < 0:
            self.internal_timer = 6
            self.give_birth()

    def give_birth(self):
        self.womb.make_baby()


@dataclass
class LanternfishSim:
    loader: Loader
    hatchery: Hatchery
    days_to_simulate: int
    print_output: bool = False
    day_timer: bool = False

    def start(self):
        data = self.loader.get_input()
        input = map(int, data.split(','))
        self.get_initial_stock(input)
        self.pass_time(self.days_to_simulate)
        total_fish = self.hatchery.count_fish()
        print(f'Total fish: {total_fish}')

    def get_initial_stock(self, input):
        for i in input:
            self.hatchery.make_baby(i)

        if self.print_output:
            print(f'Initial state: {[fish.internal_timer for fish in self.hatchery.stock]}')

    def pass_time(self, days):
        current_day = 1

        while current_day <= days:
            [fish.age_one_day() for fish in self.hatchery.stock]
            if self.print_output:
                print(f'After {current_day} days: {[fish.internal_timer for fish in self.hatchery.stock]}')
                # print(f'After {current_day} days: {self.hatchery.count_fish()} fish')
            current_day += 1


@dataclass
class LanternfishSim2:
    loader: Loader
    days_to_simulate: int
    fish_stock: dict = None

    def __post_init__(self):
        self.fish_stock = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }

    def start(self):
        data = self.loader.get_input()
        input = map(int, data.split(','))
        self.get_initial_stock(input)

        for _ in range(self.days_to_simulate):
            self.add_one_day()

        print(sum(self.fish_stock.values()))

    def get_initial_stock(self, input):
        for i in input:
            self.fish_stock[i] += 1

    def add_one_day(self):
        new_dict = {
            0: self.fish_stock[1],
            1: self.fish_stock[2],
            2: self.fish_stock[3],
            3: self.fish_stock[4],
            4: self.fish_stock[5],
            5: self.fish_stock[6],
            6: self.fish_stock[7] + self.fish_stock[0],
            7: self.fish_stock[8],
            8: self.fish_stock[0]
        }

        self.fish_stock = new_dict


if __name__ == '__main__':
    main()
