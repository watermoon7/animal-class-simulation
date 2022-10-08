board = [
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ']
        ]

class Animal():

    directions = {
            'right': [0,1],
            'left': [0,-1],
            'up': [-1,0],
            'down': [1,0],
            'up right': [-1,1],
            'down right': [1,1],
            'up left': [-1,-1],
            'down left': [1,-1]
            }
    
    def __init__(self, age, species, pos):
        self.age = age
        self.species = species
        self.foodbar = (3, 10)
        self.pos = pos
        board[self.pos[0]][self.pos[1]] = species

    def eat(self):
        self.foodbar[0] += 1

    def move(self, direction):
        self.pos = [self.pos[0] + direcrions[direction][0]][self.pos[1] + direcrions[direction][1]]

class bird(Animal):
    def __init__(self, colour, varient, age, species, pos):
        super().__init__(age, species, pos)
        self.colour = colour
        self.varient = varient

class cat(Animal):
    def __init__(self, colour, varient, age, species, pos):
        super().__init__(age, species, pos)
        self.colour = colour
        self.varient = varient

class fish(Animal):
    def __init__(self, colour, varient, age, species, pos):
        super().__init__(age, species, pos)
        self.colour = colour
        self.varient = varient

class worm(Animal):
    def __init__(self, colour, varient, age, species, pos):
        super().__init__(age, species, pos)
        self.colour = colour
        self.varient = varient


finch_1 = bird('black', 'finch', 4, 'bird', [0,1])
finch_2 = bird('blue', 'finch', 3, 'bird', [0,2])
chicken_1 = bird('brown', 'chicken', 6, 'bird', [3,1])
lion_1 = cat('burgundy', 'lion', 5, 'cat ', [6,4])
jaguar_1 = cat('orange and black', 'jaguar', 7, 'cat ', [5,5])
salmon_1 = fish('silver', 'salmon', 1, 'fish', [4,7])
salmon_2 = fish('silver', 'salmon', 0.6, 'fish', [3,7])
salmon_3 = fish('silver', 'salmon', 1.3, 'fish', [4,6])
garden_worm_1 = worm('pink', 'garden_worm', 0.05, 'worm', [3,3])

animals = [
    finch_1,
    finch_2,
    chicken_1,
    lion_1,
    jaguar_1,
    salmon_1,
    salmon_2,
    salmon_3,
    garden_worm_1
    ]

for animal in animals:
    print(animal.species)
    print(' '.join(list(str(i) for i in vars(animal).values())))
    print('')

print('\n'.join([str(row) for row in board]))

