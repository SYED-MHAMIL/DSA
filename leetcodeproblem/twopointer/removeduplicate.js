// // /**
// //  * @param {number[]} nums
// //  * @param {number} val
// //  * @return {number}
// //  */
// var removeElement = function(nums, val) {
//    nums.sort()
//    let k=0
//    let length = nums.length -1
// //    nums = [0,0,1,2,2,2,3,4], val = 2
   
// for(let i=0; i<nums.length; i++){
//     for(let j=length; j>i; j--){
//         if(nums[i] == val){
//            nums[j],nums[i] =nums[i],nums[j]
//            length-=1
//            break
//         }
//         console.log(i);
        
//         k+=1
//         break 
        
//     }
// }  
//    console.log(nums);
//    console.log(length);
   
//    return k
// };
// console.log(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))













// =============================================
// two ppoinetr  with O(n log n )complexity
// =============================================



// var removeElement = function(nums, val) {
//    nums.sort((a, b) => a - b);

//    let left= 0
//    let right = nums.length -1
//    let k =0 
//    // [0,0,1,2,2,2,3,4] , val =2 
//    // [0,0,1,4,2,2,3,2]
//    // [0,0,1,4,3,2,2,2]

//    // if (nums.length == 1 &  nums[0] == val) {
//    //    return nums.length
//    // }

//    while (left  <= right){
      
//       console.log('left',left);
//       console.log('right',right);
//         if(nums[left] === val){
//            if(nums[left] !== nums[right]){
//             k+=1
//            }
//             [nums[left], nums[right]] = [nums[right], nums[left]];

//              left+=1
//              right-=1
//         }else{
//             k+=1 
//             left+=1
//         }
//    }

   
//    return  k
// };

// console.log(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))











// =============================================
// two pointer o(n) complextiy 
// =============================================



// var removeElement = function(nums, val) {
//    nums.sort((a, b) => a - b);

//    let left= 0
//    let right = nums.length -1
//    let k =0 
//    // [0,0,1,2,2,2,3,4] , val =2 
//    // [0,0,1,4,2,2,3,2]
//    // [0,0,1,4,3,2,2,2]

//    // if (nums.length == 1 &  nums[0] == val) {
//    //    return nums.length
//    // }

//    while (left  <= right){
      
//       console.log('left',left);
//       console.log('right',right);
//         if(nums[left] === val){
//            if(nums[left] !== nums[right]){
//             k+=1
//            }
//             [nums[left], nums[right]] = [nums[right], nums[left]];

//              left+=1
//              right-=1
//         }else{
//             k+=1 
//             left+=1
//         }
//    }

   
//    return  k
// };

// console.log(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))






