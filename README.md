## BOGOSORT

This repository will contain my favorite bad sorting algorithm in all of the programming languages that I know well. Also, I think that this will be a good introduction to what languages I know and how I like to program. 

## Bogosort

As an algorithm, bogosort is not very good as it sorts by shuffling the input and it never saves any correct items in the ouput. Due to this, at even moderate input sizes (10+) bogosort can take a long time and a large number of attempts. 

Since some languages do not have a built-in shuffle function, all implementations will use the [Fisher-Yates](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) algorithm. I chose Fisher-Yates becuase the first time I wrote bogosort I was using Python and the built-in `shuffle()` uses the algorithm. Even when a language has its own shuffle function available, I will still reimplement Fisher-Yates on my own because I think that it shows some really interesting aspects of programming languages and how each one interacts with randomness. 

## Language Specific Notes

Most languages have conventions, I will try to stick to those were possible and make sure that things such as function names, variable names, and most other aspects as the languages demand. However, to keep the repository simple (at least for now), all languages will be kept to a single file. 

#### Languages

- [ ] C
- [x] JavaScript
- [x] PHP
- [x] Python
- [ ] Shell (bash)
