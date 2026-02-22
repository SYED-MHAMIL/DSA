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

var removeElement = function (nums, val) {
  let left = 0;
  let right = nums.length - 1;
  let k = 0;

  while (left <= right) {
    // nums = [0,1,2,2,3,0,4,2], val = 2
   //  here two things happens 

   // first if val is not equal to current val :
            //   also update k th value 
          //  here we just updae the left pointer 
   // else thing happens which is if val qual :
         //  to thing another happens  :
                  // if curr val is qual to swap: 
                        // we will updaee right ppointer after swaps 
                     //else: 
                        //   modify update why it work becuse we have swaps remove element successfully for that place /
      if (val == nums[left]) {
         if (nums[left] == nums[right]) {
               right-=1
         } else {
            [nums[left],nums[right]]=[nums[right],nums[left]]
            k+=1
            left+=1
            right-=1
         }
      } else {
         left+=1
         k+=1
      }
    
  
}
  return k;
};

console.log(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2));