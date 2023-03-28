# parseChallenge
This is a Python script that replaces each word in a sentence with a modified version of the word. The modified word is created by applying the following rules:

- The first letter of the word is preserved.
- The number of distinct characters between the first and last character of the word is determined.
- The last letter of the word is preserved.

The resulting modified words are then combined to form the modified sentence.

## Installation
Clone the repository and install the dependencies:
```
$ git clone https://github.com/lmtuberquia/parseChallenge.git
$ cd parseChallenge
$ pip install -r requirements.txt
```

## Usage
To use the script, run the replacesentence.py file and pass in the input file to be processed:
```
$  python replacesentence.py --file input.txt
```

## Input file format
The input file should contain one or more sentences, each on a separate line.

### Example

#### Input
```
The quick brown fox jumps over the lazy dog.
```

#### Output
```
T1e q4k b3n f1x j3s o2r t1e l2y d1g.
```

## Tests
To run the tests, run the following command:
```
$ pytest
```




