def main():
    newJar = Jar()
    print(str(newJar.capacity))
    newJar.deposit(8)
    print(f"cookies deposited = {str(newJar)}")
    newJar.withdraw(3)
    print(f"cookies after withdraw = {str(newJar)}")


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if self.capacity < 0 or self.capacity > 12:
            raise ValueError("init.Error => too many")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < self.capacity:
            self.size += n
        else:
            raise ValueError("deposit.Error => too-many")

    def withdraw(self, n):
        if n <= self.capacity:
            self.size -= n
        else:
            raise ValueError("withdraw.Error => not-enough")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size


main()
