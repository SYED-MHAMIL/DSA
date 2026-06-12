// find the missing and repeating number in an array of n elements which contains numbers from 1 to n

// Input: arr[] = {3, 1, 3}
// Output: Missing = 2, Repeating = 3
// Input: arr[] = {4, 3, 6, 2, 1, 1}
// Output: Missing = 5, Repeating = 1

// function findMissingAndRepetiveNumber(nums) {
//     let freqs = new Array(nums.length+1).fill(0) ; // [0,1,0,2]
//     let repeating=-1
//     let missing = -1
    
//     for (let i = 0; i < nums.length; i++) {
//         const element = nums[i];
//         freqs[element]++;
//     }  
//     // console.log(freqs);
    
//     for (let i = 1; i < freqs.length; i++) {
//         // const element = nums[i];
//         if (freqs[i] == 2) {
//               repeating = i
//         }
//         if(freqs[i] == 0){
//            missing = i 
//         }      
//     }
//     console.log({repeating,missing});
    
//     return [repeating,missing]  
       
// }
// findMissingAndRepetiveNumber([3,1,2,5,3]) 
//  the missing number


// function findMissingAndRepetiveNumber(nums) {
// // we need just two thing:   
// //  s - sn 
// // s2 - s2n 
//   let  n  =nums.length
//   let s2n  = (n*(n+1)*((2*n)+1))/6
//   let  sn= (n*(n+1))/2 
   

// let s=0;
// let s2=0;

// for (let i= 0;i < n;i++) {
//     s+=nums[i]      
//     s2+=nums[i] * nums[i]
// }


// //  find s-sn  = x-y 
// let val1 = s-sn

// // let's find (s2 -s2n)  == x2-y2= (x-y)(x+y)
// let val2 = s2 - s2n // x2-y2
// // x+y by using  x+y = x2- y2 / x-y
// let val3 = val2 / val1  
// // let's add up both equation
// let x = (val1 + val2) /2   
// let y = x-val1
  
// return [x,y]

// }



//




