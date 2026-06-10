

//  lower bound

// Question: Given a sorted array of integers and a target value, return the index of the first occurrence of the target value in the array. If the target value is not found in the array, return -1.

// Example:
// Input: nums = [1,2,6,7,7,8,9], target = 5
// Output: 4    
// exmaple [1,2,3,4,5,5] target = 5
// output 4


// const lowerBound = (nums,target)=>{
//      let low =  0;
//      let high = nums.length;
//      let ans= nums.length;
//      while(low <= high){
//          let mid = Math.floor((low+high)/2)
//          if ( nums[mid] >= target) {
//                ans = mid
//                high=mid -1
//          }else{
//               low= mid+1
//          }
//      }
//      return ans
// }




// / recursive away 




// const lowerBound = (nums,target)=>{
//      let low =  0;
//      let high = nums.length - 1;
//      let ans= nums.length;
//      function solve(low,high){
//           if (low >= high) {
//              return ans
//           }
//           let mid = Math.floor((low+high)/2)

//           if (nums[mid] >= target) {
//                ans = mid;
//                return solve(low,mid- 1)
//           }else{
//             return solve(mid -1,low)
//           }
//      }
//      return solve(low,high)
//      console.log(ans);
     
// }
// console.log(lowerBound([1,6,7,7,7,8,9],5));


