class Dictionary:
    def __init__(self) -> None:
        self.values = set()

    def insert(self, value):
        self.values.add(value)

    def find(self, value):
        if value in self.values:
            print('yes')
        else:
            print('no')


dic = Dictionary()
n = int(input())

for i in range(n):
    line = input().split()
    command = line[0]
    value = line[1]

    if command == 'insert':
        dic.insert(value)
    elif command == 'find':
        dic.find(value)
