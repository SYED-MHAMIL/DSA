//  Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

// Example 1:


// Input: heights = [2, 1, 5, 6, 2 , 3 ]
                //  [5, 5 ,6,-1,-1,  3 ]
                //  [-1,-1,1, 5, 1,  2 ]   
// if i take 
// Output: 10
// Explanation: The above is a histogram where width of each bar is 1.
// The largest rectangle is shown in the red area, which has an area = 10 units.
// Example 2:


// Input: heights = [2,4]
// Output: 4


// from brute force  

// function largestRecArea(array) {
//     let res = 0 
//     for (let index = 0; index < array.length; index++) {
//         const element = array[index];
//         for (let j = index; j < array.length; j++) {
//             const subs = array.slice(index,j+1);
//             const subLenght =  subs.length; 
//             const min = Math.min(...subs)
//              let  area =min * subLenght  
//            if(res <area){
//                console.log(subs);
               
//                res = area       
//            }             
//         }
//     }
//     return res
// }

// console.log(largestRecArea([2,4]))