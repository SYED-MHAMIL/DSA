/**
 * @param {Number[]} arr
 * @returns {Number}
 */
class Solution {
    maxLength(arr) {
        // code here
        let maxLen = 0
        let firstseen = new Map() // SAVE PREFIX SUM WITH INDEX FOR THE FIRST TIME FOR EACH SUM IF NOT SEEN BEFORE AND IF SEEN BEFORE CALCULATE THE LENGTH AND UPDATE MAXLEN BECAUSE THE SUM IN BETWEEN IS ZERO
        let sum =0 
        for(let i=0; i < arr.length; i++){
            sum+=arr[i]
            if(sum == 0){
                maxLen= i+ 1
            }else{
                // a;reawdy there
                if(firstseen.has(sum)){
                    maxLen = Math.max(maxLen,i - firstseen.get(sum))
                }else{
                      firstseen.set(sum,i)                    
                }
            }
        }
               
        

        return maxLen
    }
}

// the time complexity is O(n) and space complexity is O(n) because of the map

// TEST CASES
// let sol = new Solution()
// console.log(sol.maxLength([1, -1, 3, 2, -2, -3, 3])) // 5
// console.log(sol.maxLength([1, 2, 3, -6, 4, -2])) // 4
// console.log(sol.maxLength([1, 2, 3, -6, 4, -2, 2])) // 4
// console.log(sol.maxLength([1, 2, 3, -6, 4, -2, 2, -4])) // 8




















// **************************************************************
//               longest subbarray with qual sum 
// **************************************************************

// Given an array arr[] of size n containing integers, the task is to find the length of the longest subarray having sum equal to the given value k.

// Note: If there is no subarray with sum equal to k, return 0.

// Examples: 

// Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
// Output: 6
// Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

// Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
// Output: 5
// Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.

// Input: arr[] = [10, -10, 20, 30], k = 5
// Output: 0
// Explanation: No subarray with sum = 5 is present in arr[].



const longestSubarrayEqualSum = (arr,k)=>{
    let max =0 
    let hashmap = new Map();
    let  sum =  0 
    // [10, 5, 2, 7, 1, -10] ,k =15
    for(let i=0; i<arr.length; i++){
         sum+=arr[i]
         hashmap.set(sum,i)
        //  10,15,17,24,25,15    
         if(sum == k){
              max= i+ 1
         }else{
             if (hashmap.has(sum -k) ) {
                 let val = hashmap.get(sum- k)
                 max = Math.max(max,i - val)
             }
         }

         
    }
   return max
 }

 console.log(longestSubarrayEqualSum([10, 5, 2, 7, 1, -10], k = 15));
 