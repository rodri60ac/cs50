class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    jar.deposit(3)
    jar.deposit(5)
    print(jar)


if __name__ == "__main__":
    main()