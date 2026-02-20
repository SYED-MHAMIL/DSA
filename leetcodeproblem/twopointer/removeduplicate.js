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







// two ppoinetr  



var removeElement = function(nums, val) {
   nums.sort()
   let left= 0
   let right = nums.length -1
   let k =0 
   while (left  < right){
        if(nums[left] === val){
           let temp = nums[left];
nums[left] = nums[right];
nums[right] = temp;
             left+=1
             right-=1
        }else{
            k+=1 
            left+=1
        }
   }
   console.log(nums);
   
   return  k
};

console.log(removeElement(nums = [0,1,2,2,3,0,4,2], val = 3))
