## Blind 75 

https://leetcode.com/list/xi4ci4ig/

### 1. Two Sum
Use a hashmap to keep the entries and their indices, add them as traversing through the array. 

Traverse through the array and check if the (target - current val) exists in the hash map.
- Time complexity O(n) - Have to only go through the array once
- Space complexity O(n) - The hash map needs space to store n number of values at the worst case 

### 2.  Longest Substring Without Repeating Characters

Use a sliding window to keep track of the substring we are working with. 
While iterating through the string use a Set to make sure there are no duplicates in the sliding window
and update the window otherwise 

- Time complexity O(n)
- Space complexity O(n)
