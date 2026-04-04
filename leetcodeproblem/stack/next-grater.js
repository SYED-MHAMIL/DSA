/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
// var nextGreaterElement = function(nums1, nums2) {

//     let result = new Array(nums1.length).fill(-1)
//     let stack = []
//     let nums1Idx = {}
//    for (let index = 0; index < nums1.length; index++) {
//     const element = nums1[index];
//            nums1Idx[element] = index
    
//    }
//    console.log(nums1Idx);
   

//     for(let i=0;  i< nums2.length; i++){
//         let curr = nums2[i]
//         while(stack.length >  0 &&  stack[stack.length -1] < curr ){
//                 let element  =  stack.pop()
//                 let idx =  nums1Idx[element]
//                 result[idx] = curr

//         }
//         // is this nmber is exits in num1
//         // console.log(curr);
        
//         if (nums1Idx[curr] !== undefined) {
//             console.log(nums1Idx[curr]);            
//             stack.push(curr)
//         }
        
// }
//         return result
// }

// console.log(nextGreaterElement(nums1 = [2,4], nums2 =[1,2,3,4])); // 4,2,1



// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Given an array arr[], find the Previous Greater Element (PGE) for every element in the array.

// The Previous Greater Element of an element x is defined as the first element to its left in the array that is greater than x.
// If no such element exists for a particular position, the PGE should be considered as -1.
// Examples: 

// Input: arr[] = [10,4, 2, 20, 40, 12]
// Output: [-1, 10, 4, -1, -1, 40]
// Explanation:
// For 10 → No elements on the left → -1
// For 4 → Previous greater element is 10 → 10
// For 2 → Previous greater element is 4 → 4
// For 20 → No element on the left greater than 20 → -1
// For 40 → No element on the left greater than 40 → -1
// For 12 → Previous greater element is 40 → 40

// Input: arr[] = [10, 20, 30, 40]
// Output: [-1, -1, -1, -1]
// Explanation: Since the array is strictly increasing, no element has a greater element before it. Hence, all positions are assigned -1


// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// 

// var prevGreaterElement = function(array) {
//         // 
//      let  stack =  [];
//      let res = []
//       for (let  index = 0;  index
//  < array.length;  index++) {
//         const element = array[ index];
//         while (stack.length >  0   &&  array[stack[stack.length -1]] < element) {
//                  stack.pop()
//         }
//         if(stack.length > 0){
//                 res.push(array[stack[stack.length -1]]) 

//         }else{
//                 res.push(-1)

//         }
//         stack.push(index)
//       }
//      return res

// }
// console.log(prevGreaterElement([10, 4, 2, 20, 40, 12]));

