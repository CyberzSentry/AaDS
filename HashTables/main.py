from HashTables import  hashTables
from Sources import fileDriver
import random

htl = hashTables.HashTableLinear(1000000, 20)
htd = hashTables.HashTableDouble(1000000)

nums = fileDriver.getIntArrayPath("../Sources/set_of_1050000_random_numbers.txt")
searched = fileDriver.getIntArrayPath("../Sources/set_of_1050000_random_numbers_for_search_miss.txt")

for i in range(500000):
    htl.insert(nums[i])
    htd.insert(nums[i])

for i in range(50000):
    htl.search(nums[random.randint(0, 500000 - 1)])
    htd.search(nums[random.randint(0, 500000 - 1)])

print("------50% fill actor------\n\n")
print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.5))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.5))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.5))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.5))

htl.reset()
htd.reset()

for i in range(50000):
    htl.search(searched[random.randint(0, 500000 - 1)])
    htd.search(searched[random.randint(0, 500000 - 1)])

print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.5))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.5))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.5))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.5))
print("\n\n\n\n")
htl.reset()
htd.reset()

for i in range(500000, 700000):
    htl.insert(nums[i])
    htd.insert(nums[i])

for i in range(70000):
    htl.search(nums[random.randint(0, 700000 - 1)])
    htd.search(nums[random.randint(0, 700000 - 1)])

print("------70% fill actor------\n\n")
print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.7))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.7))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.7))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.7))

htl.reset()
htd.reset()

for i in range(70000):
    htl.search(searched[random.randint(0, 700000 - 1)])
    htd.search(searched[random.randint(0, 700000 - 1)])

print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.7))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.7))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.7))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.7))
print("\n\n\n\n")

htl.reset()
htd.reset()

for i in range(700000, 800000):
    htl.insert(nums[i])
    htd.insert(nums[i])

for i in range(80000):
    htl.search(nums[random.randint(0, 800000 - 1)])
    htd.search(nums[random.randint(0, 800000 - 1)])

print("------80% fill actor------\n\n")
print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.8))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.8))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.8))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.8))

htl.reset()
htd.reset()

for i in range(80000):
    htl.search(searched[random.randint(0, 800000 - 1)])
    htd.search(searched[random.randint(0, 800000 - 1)])

print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.8))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.8))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.8))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.8))
print("\n\n\n\n")

htl.reset()
htd.reset()

for i in range(800000, 900000):
    htl.insert(nums[i])
    htd.insert(nums[i])

for i in range(90000):
    htl.search(nums[random.randint(0, 900000 - 1)])
    htd.search(nums[random.randint(0, 900000 - 1)])

print("------90% fill actor------\n\n")
print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.9))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.9))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.9))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.9))

htl.reset()
htd.reset()

for i in range(90000):
    htl.search(searched[random.randint(0, 900000 - 1)])
    htd.search(searched[random.randint(0, 900000 - 1)])

print("--------Search hit--------")
print("Linear:\t", htl.sHit / ((htl.size / 10) * 0.9))
print("Double:\t", htd.sHit / ((htd.size / 10) * 0.9))
print("--------Search miss-------")
print("Linear:\t", htl.sMiss / ((htl.size / 10) * 0.9))
print("Double:\t", htd.sMiss / ((htd.size / 10) * 0.9))
print("\n\n\n\n")

print("Done")
