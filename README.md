# Algorithm Practices

Usage:

```
python sort.py -h
usage: Sort Algorithm [-h] [-sa {CS,IS,QS,RMS,IMS}] {asc,desc} [array ...]

Run implemented sort algorithm

positional arguments:
  {asc,desc}            choose sort order
  array                 input array of integer to sort, separate by space

options:
  -h, --help            show this help message and exit
  -sa {CS,IS,QS,RMS,IMS}, --sort-algorithm {CS,IS,QS,RMS,IMS}
                        choose implemented algorithm to run: {'CS': 'Counting Sort', 'IS': 'Insertion Sort', 'QS': 'Quick Sort',
                        'RMS': 'Recursive Merge Sort', 'IMS': 'Iterative Merge Sort'}
```

Example:
```
python sort.py -sa CS asc 4 8 99 23 11 56
Chosen sort algorithm: Counting Sort
Here is some info about Counting Sort: 

    Implementation of counting sort algorithm for sorting array of intergers
    Time complexity: O(n + k)
        n (actually 2*n): one pass over arr to find min, max
             one pass over arr to fill in counting array
        k = max - min: one pass over counting array (with k elements) to create result array
    
Input array: [4, 8, 99, 23, 11, 56]
Sorted array: [4, 8, 11, 23, 56, 99]
```