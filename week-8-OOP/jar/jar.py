# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    jar.py                                            #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/8/jar/


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.deposit(1)
    jar.deposit(1)
    print(jar)
    jar.withdraw(5)
    print(jar._size)
    print(jar)


if __name__ == "__main__":
    main()
