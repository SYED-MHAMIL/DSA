// Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10power9 + 7.

 

// Example 1:

// Input: arr = [3,1,2,4]
// Output: 17
// Explanation: 
// Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
// Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
// Sum is 17.


// function MinimumsSubarray(array) {
//      let minSumarr = 0
//      let mode = 10^ + 7
//      for (let i = 0; i < array.length; i++) {
//         for (let j = i; j < array.length; j++) {
//             const sbr = array.slice(i,j+1);
//             minSumarr+= Math.min(...sbr) %  mode
                   
//         }
//      }
//      return minSumarr
// }

// console.log(MinimumsSubarray([11,81,94,43,3]));



