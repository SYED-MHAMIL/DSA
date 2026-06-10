// *********************************************************
// ******************* UPPER BOUND *************************
// *********************************************************





function upperBound(nums,target) {
     let low = 0
     let high = nums.length - 1
     let res  = nums.length
     while (low <= high) {
         let mid = Math.floor((low+high)/2);
         if (nums[mid] > target) {
              res = mid;
              high = mid -1
         } else {
            low = mid + 1
         }     
     }
     return res
}


console.log(upperBound([1,2,3,4,5,7,7,8,8,8,9,9,11,11,11],1));





