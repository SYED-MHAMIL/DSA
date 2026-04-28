// var merge = function(nums1, m, nums2, n) {
//    if(n==0){
//       return nums1
//    } 

//    if(m == 0){
//       return nums2
//    }  

//     for(let i=m; i<m+n;  i++){        
//               nums1[i] =nums2[i-m   ]
//     }
//     return  nums1.sort((a,b)=>a-b)
// };



/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
// check which is greather and equal
  let i=0
  let j =0
  let k=0

  while(i<m &&j<n){
     if(nums1[i] < nums2[j]){
        console.log('nums1',i);
          nums1[k++] = nums1[i++]
        console.log('after nums1 update',nums1);

          
     }else if(nums1[i] < nums2[j]){

     }else{
        console.log('nums2',j);
         nums1[k++] = nums2[j++]
        console.log('after nums2 update',nums1);

     }
  }

   while(i<m){
     nums1[k++] = nums2[i++]
   }
   while(j<n){
     nums1[k++] = nums2[j++]
   }
   return nums1
};

console.log(merge(nums1=[1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3));

// let i =0 
// let j=0 
// let k=0 

// if nums1[i] < nums[2]
            // nums1[k++] = nums1[i++]
// else:
            //           nums1[k++] = nums2[j++]

// [1,2,2]
// k=2
// i=2
// j=1


