# GildedRose Refactoring Kata - Python Solution
This is my attempt to solve the [Gilded Rose refactoring kata by Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata) in python. The specification of the challenge can be found [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt).

### Decomposing the challenge:
1. Gilded Rose is a business that sells 'items'. The items are identified by name and have following characteristics:
 - A SellIn value (denotes the number of days till the item needs to be sold)
 - A Quality value (denotes the value of the item)
 - At the end of each day the system lowers the SellIn value and changes the Qality by a certain delta (positive or negative, this depends on type of item)

2. At the moment the business sells the following types of items:
 - Regular items (general default items without any special characteristics)
 - Aged Brie
 - Sulfuras
 - Backstage passes

3. The business is going to introduce a new category of items called "Conjured" which has its own special characteristics and hence won't fall under the regular items (**the program needs to be updated for this change**). 


#### The daily change (Delta) in Quality specific to items can be tabulated as:

| Item  | Delta | Minimum | Maximum |
| ------------- | ------------- |------------- |------------- |
| Default| -1 | 0 | 50 |
| Aged Brie| +1 | 0 | 50 |
| Sulfuras| 0 | 80 | 80 |
| Backstage passes| Specific to SellIn value* (see Note1*)  | 0 | 50 |
| Conjured| -2 | 0 | 50 |

Note1* : - "Backstage passes", increases in Quality as its SellIn value approaches (+1);
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	Quality drops to 0 after the concert.
 
 ### Approach:
1. Decompose the problem logically and document it
2. Run the provided source code
3. Write a number of test cases for unit testing all the aspects of provided source code
4. Refactor the code while making sure all the test cases written in previous step pass througout all the stages of refactoring
5. Add unit tests for logic to be added ('Conjured Items')
6. Write the logic for Conjured items

### Setup:
- The task was done and tested in **Python 3.8.2** (Windows10)
- The github workflow builds and tests the task for python versions **3.6, 3.7 & 3.8** (ubuntu-latest)

To setup and activate virtual environment:
```
  python -m venv gilded_rose
  
  gilded_rose\Scripts\activate.bat

```
  
To run the unit tests: 
```
  cd solution
  
  python -m unittest tests/test_gilded_rose.py -v

```
