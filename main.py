class First:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return repr('hello ' + self.name + ' are you ' + self.age + '?')

    def __str__(self):
        return str('hello ' + self.name + ' do you live in ' + self.address + '?')


class FirstAgain:
    def __init__(self, weather, degrees):
        self.weather = weather
        self.degrees = degrees

    def __call__(self, warning):
        print(f'today is {self.weather}, it`s about {self.degrees} degrees')
        print(warning)


first = First
print(first(name='Ivan', age='5', address=''))
print(first(name='Ivan', age='',  address='Ivankiv'))

first_again = FirstAgain(weather='rainy', degrees=-8347)
print(first_again('take an umbrella'))


class Second:
    def __init__(self, listt):
        self.listt = listt

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.listt[key] = value

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.listt[key]


second = Second(['apple', 'watermelon'])
print(second[1])
second[1] = 'orange'
print(second[1])


class Third:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.filename = open(self.filename, self.mode)
        return self.filename

    def __exit__(self, exc_type, exc_value, traceback):
        self.filename.close()


with Third('text.txt', 'w') as file:
    file.write('hello')
