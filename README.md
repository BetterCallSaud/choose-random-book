# Choose a Random Book
A Python script to randomly choose a book (PDF) from the given directory. This script uses the Python packages of `time, os & random`.

From `os`, I imported `listdir, isfile and join`. 

`listdir` is used to list out all the files in the directory provided, if a proper file exists, which is done using `isfile` and `join`.

Then we randomly choose an index in the range of the number of books and select a book.

## Why did I create this?
I had like 100s of PDFs of all kinds of books stored in `D:/Books` on my system. Whenever I wanted to read a book, I used to spend minutes of my time deciding what I wanna read. So I thought...

*Let randomness take care!*
