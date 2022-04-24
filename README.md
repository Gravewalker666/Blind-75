## Blind 75 

https://leetcode.com/list/xi4ci4ig/

### 1. Two Sum
Use a hashmap to keep the entries and their indices, add them as traversing through the array. Traverse through the 
array and check if the (target - current val) exists in the hash map.
- Time complexity O(n) - Have to only go through the array once
- Space complexity O(n) - The hash map needs space to store n number of values at the worst case 

### 2.  Longest Substring Without Repeating Characters

Use a sliding window to keep track of the substring we are working with. 
While iterating through the string use a Set to make sure there are no duplicates in the sliding window
and update the window otherwise 

- Time complexity O(n)
- Space complexity O(n)

### 3.  Longest Palindromic Substring

Iterate through the array for each character, Assume the current position is the mid-point and check if it holds the 
values of a palindrome expanding outwards, use two pointers to do this. Consider even and odd length strings two different 
cases.

- Time complexity O(n^2)
- Space complexity O(n)

### 4. Container With Most Water

Fix two pointers at the two ends of the array to begin with. Check the area those two heights make and 
update the max area variable. Shift the pointers to the middle by only moving the pointer that has the shortest height. 
Do this until two pointers meet

- Time complexity O(n)
- Space complexity O(n)

### 5. Three sum

First sort the array. Start iterating through the array starting from the first index. Inside the loop put two pointers 
to i + 1 and the last element on the array as l and r. if the sum of i, l, and r is 0 add it to the result set and move 
increase the left pointer (avoid duplicates by skipping duplicates on this step). If it's larger than 0 move the right 
pointer towards left to decrease the sum, if it's the other way around increase the value of sum by moving the left 
pointer to the right

- Time complexity O(n^2)
- Space complexity O(n)

### 6. Remove Nth Node From End of List

Add a dummy node to the front of the list. Have two pointers, left and right, at first pointing to the dummy node and 
n + 1 nodes away from the dummy node respectively. Move the pointers one node at a time until the right pointers reaches 
the end of the list. Now the left.next is pointing to the node we need to remove. 

- Time complexity O(n)
- Space complexity O(1)
