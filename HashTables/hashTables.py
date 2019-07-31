class HashTableLinear:
    """Hash table class"""

    def __init__(self, size, i):
        print("Hash table constructed")
        self.table = [None] * size
        self.size = size
        self.i = i
        self.sHit = 0
        self.sMiss = 0

    def insert(self, element):
        x = element % self.size

        while self.table[x] is not None:
            x = (x + self.i) % self.size

        self.table[x] = element

    def search(self, element):
        y = 1
        x = element % self.size

        while self.table[x] != element:
            if self.table[x] is None:
                self.sMiss += y
                return
            x = (x + self.i) % self.size
            y = y + 1

        self.sHit += y

    def reset(self):
        self.sHit = 0
        self.sMiss = 0


class HashTableDouble:
    """Hash table class"""

    def __init__(self, size):
        print("Hash table constructed")
        self.table = [None] * size
        self.size = size
        self.sHit = 0
        self.sMiss = 0

    def insert(self, element):
        i = 0
        h1 = self.h1(element)
        h2 = self.h2(element)

        x = (h1 + (i * h2)) % self.size

        while self.table[x] is not None:
            i += 1
            x = (h1 + (i * h2)) % self.size

        self.table[x] = element

    def search(self, element):
        i = 0
        y = 1
        h1 = self.h1(element)
        h2 = self.h2(element)

        x = (h1 + (i * h2)) % self.size

        while self.table[x] != element:
            if self.table[x] is None:
                self.sMiss += y
                return
            y += 1
            i += 1
            x = (h1 + (i * h2)) % self.size

        self.sHit += y

    def h1(self, element):
        return element % self.size

    def h2(self, element):
        return ((2 * element) % (self.size - 1)) + 1

    def reset(self):
        self.sHit = 0
        self.sMiss = 0


class HashTableLinearString:
    """Hash table class"""

    def __init__(self, size, i):
        print("Hash table constructed")
        self.table = [None] * size
        self.size = size
        self.i = i
        self.sHit = 0
        self.sMiss = 0

    def insert(self, element):
        temp = hash(element)
        x = temp % self.size

        while self.table[x] is not None:
            x = (x + self.i) % self.size

        self.table[x] = element

    def search(self, element):
        y = 1
        temp = hash(element)
        x = temp % self.size

        while self.table[x] != element:
            if self.table[x] is None:
                self.sMiss += y
                return
            x = (x + self.i) % self.size
            y = y + 1

        self.sHit += y

    def reset(self):
        self.sHit = 0
        self.sMiss = 0


class HashTableDoubleString:
    """Hash table class"""

    def __init__(self, size):
        print("Hash table constructed")
        self.table = [None] * size
        self.size = size
        self.sHit = 0
        self.sMiss = 0

    def insert(self, element):
        i = 0
        temp = hash(element)
        h1 = self.h1(temp)
        h2 = self.h2(temp)

        x = (h1 + (i * h2)) % self.size

        while self.table[x] is not None:
            i += 1
            x = (h1 + (i * h2)) % self.size

        self.table[x] = element

    def search(self, element):
        i = 0
        y = 1
        temp = hash(element)
        h1 = self.h1(temp)
        h2 = self.h2(temp)

        x = (h1 + (i * h2)) % self.size

        while self.table[x] != element:
            if self.table[x] is None:
                self.sMiss += y
                return
            y += 1
            i += 1
            x = (h1 + (i * h2)) % self.size

        self.sHit += y

    def h1(self, element):
        return element % self.size

    def h2(self, element):
        return ((2 * element) % (self.size - 1)) + 1

    def reset(self):
        self.sHit = 0
        self.sMiss = 0