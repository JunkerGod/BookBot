## IPO Table:

| Input                                          | Process                                                                                             | Output                                                 |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| CLI arguments in `sys.argv`                    | Check that the list contains at least two entries                                                   | Book path/ usage message and exit status `1`           |
| File path from `sys.argv[1]`                   | `get_book_text()`Open's file and read  contents                                                     | Book text as string                                    |
| Book text                                      | `Count_words()` splits the text into words and counts them                                          | total number of words                                  |
| Book text                                      | `character_count()` converts the characters to lowercase and counts each occurence of the character | Dictionary containing the characters and there  counts |
| Character Count dictionary                     | `char_dict_to_sorted_list()` sorts the characters from highest to lowest count                      | Sorted list of tuples                                  |
| Book path, word count, sorted character counts | `print_report()` formats results and includes only letters in the report                            | Formatted cli report                                   |
|                                                |                                                                                                     |                                                        |

## Flow Diagram: 

![[DataFlowDiagram.png]]

## Design decisions and justifications


| Desision                                    | Justification                                                                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------- |
| Read the path from `sys.argv[1]`            | supports different books without having to change the code                            |
| Check argument length before accessing path | prevents index error and gives user instructions when no path is given                |
| seperating statisitics into `stats.py`      | keeps calculations reusable                                                           |
| Convert each character into lowercase       | combines uppercase and lowercase of each letter so they're seen as the same character |
| converting dictionary entries into tuples   | gives the report an ordered list of character:count pairs.                            |
| using `sort_on` w `reverse=true`            | sorts by the count at index 1 and orders the larger counts first                      |
| using `isalpha()`                           | only prints out alphabetic characters                                                 |
| formatting using `print report`             | keeps report headings and outputs together, while main does all the work              |
|                                             |                                                                                       |
|                                             |                                                                                       |
## Test Cases


| Input                                                        | Expected                              | Output                                                                      |
| ------------------------------------------------------------ | ------------------------------------- | --------------------------------------------------------------------------- |
| Ran with an empty file, `python main.py books/emptyfile.txt` | 0 words                               | Found 0 total words                                                         |
| Ran  `python main.py non-existant/path`                      | Error message                         | FileNotFoundError: [Errno 2] No such file or directory: 'non-existant/path' |
| Ran `python main.py books/mobydick.txt`                      | 215,838 words                         | Found 215838 words                                                          |
| Ran ` python main.py books/frankenstein.txt `                | 75,767 words                          | Found 75767 total words                                                     |
| Ran `python main.py books/prideandprejudice.txt `            | 130,410 words                         | Found 130410 total words<br>                                                |
| Ran with no path provided ` python main.py`                  | Usage: python3 main.py <path_to_book> | Usage: python3 main.py <path_to_book>                                       |
| Ran with file containing one word                            | 1 word                                | Found 1 total words                                                         |
| Ran with file only containing 4 numbers                      | 4 words                               | found 4 total words                                                         |
|                                                              |                                       |                                                                             |
## Reflection on Challenges and Solutions

### Organising Data for the Report:
The dictionary was useful for counitng counts, but the output needed characters ordered by frequency. Converting the dictionary into a list of tuples and using the sort_on function solved this. However it was difficult converting the dictionary to tuples and I had to go back to previous BootDev lessons to revise it. 

### Calling the report function:
Originally I had `print(print_report)` to print the report but instade it printed the function instead of producing the report. Replacing it with `print_report(path, num_words, sorted_characters)` executed the function and produced the report. 

### Refactoring: 
It was difficult understanding how to import the functions from one python file to another. In the end I understood after reading the BootDev documentation again. 


