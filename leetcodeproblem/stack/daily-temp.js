//  see in the solution we can get the answer from the question as well so lets go through with solution 
// /**
//  * @param {number[]} nums
//  * @return {number[]}
//  */
// var nextGreaterElements = function(nums) {
//     let stack = []
//     let res = new Array(nums.length).fill(-1) 
//     for(let i=0; i<num.length; i++){
//     while(stack && nums[stack[stack.length -1]] < nums[i]){
//          const pop_el = stack.pop()
//          res[pop_el]=nums[i]
//     }
//     stack.push(i)
//     }
//      if(stack){
//        res[]
//      }
    
// };

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    let stack = []
    let res = new Array(nums.length).fill(-1)
    let n= nums.length 
 
    for(let i=0; i<n*2; i++){
        console.log(i)
    while(stack && nums[stack[stack.length -1]] < nums[i%n]){
         const pop_el = stack.pop()
         console.log("opo",pop_el)
         res[pop_el]=nums[i%n]
    }

    if(i < n){
     stack.push(i%n)
    }
   
    }

   return res   
    
};

console.log(nextGreaterElements([3,1,2,4]))


