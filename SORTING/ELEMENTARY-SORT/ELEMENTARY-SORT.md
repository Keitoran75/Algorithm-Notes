# Elementary Sorts
Primary concern is algorithms for rearranging *arrays* of *items* where each item contains a *key*. The objective of the sorting algorithm is to rearrange the items suach that their keys are ordered acccording to some well-defined ordering rule.

## Selection sort
* Find the smallest item in the array and exchange it with the first entry
* Find the next smallest item and exchange ut with second entry

Continue in this way until the entire array is sorted. This function works by repeatedly selecting the smallest remaining item.
The number of exchanges is *N*. Thus, the running time is dominated by the number of compares.
For each *i* from 0 to *N - 1*, there is one exchange and *N - 1 - i* compares, so the totals are *N* exchanges and *(N -1) + (N - 2) + ... + 2 + 1 + 0 = N(N-1)/2* ~ *N^2 /2* compares.

IN SUMMARY, selection sort is characterized by the following two signature properties:
* *Running time is insensitive to input.* The process of finding the smallest item on one pass through the array does not give much information about where the smallest item might be on the next pass.
* *Data movement is minimal.* Each of the *N* exchanges the value of two array entries, so selection sort uses *N* exchanges - the number of array accesses is a *linear* function of the array size.

## Insertion sort
As in selection sort, the items to the left of the current index are in sorted order during the sort, but they 
are not in their final position, as they may have to be moved to make room fot smaller items encountered later.
The array, however, fully sorted when the index reaches the right end.

Insertion sort uses ~*N^2/4* compares and ~*N^2/4* exchanges to sort a randomly ordered array of length *N* with distinct keys, 
on the average. The worst case is ~*N^2/2* compares and ~*N^2/2* exchanges and the best case is *N-1* compares and 0 exchanges.
* Unlike that of selection sort, the running time of insertion sort depends on the initial order of the items in
 the input.

Consider the concept of a *partially* sorted array: An *inversion* is a pair of entries that are out of order in the array.
If the number of inversions is less than a constant multiple of the array size, then the array is *partially sorted*.

Insertion sorts is an efficient method for such arrays:
* An array where each entry is not far from its final position
* A small array appended to a large sorted array
* An array with only a few entries that are not in place.

## Shell sort
Insertion sort is slow for large unordered
arrays because the only exchanges it does involve adjacent entries, so items
can move through the array only one place at a time. For example, if the item with the
smallest key happens to be at the end of the array, *N - 1* exchanges are needed to get that
one item where it belongs.

The idea is to rearrange the array to give it the property that taking every *h*th entry
(starting anywhere) yields a sorted subsequence. Such an array is said to be *h-sorted*. Put
another way, an h-sorted array is h independent sorted subsequences, interleaved together. By h-sorting for some large values 
of h, we can move items in the array long distances and thus make it easier to
h-sort for smaller values of h.

The implementation
in Algorithm 2.3 on the facing page uses the sequence of decreasing values ½(3k1),
starting at the largest increment less than N/3 and decreasing to 1.