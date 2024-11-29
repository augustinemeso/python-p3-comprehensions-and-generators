# list_comprehension.py

def return_evens(seq):
    return [x for x in seq if x % 2 == 0]

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]

# Add test calls under the main condition
if __name__ == "__main__":
    print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Should print: [0, 8]
    print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))  # Should print: ["Hello!", "I'm doing great!", "Python is fun!"]
