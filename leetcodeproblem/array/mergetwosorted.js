var merge = function(nums1, m, nums2, n) {
   if(n==0){
      return nums1
   } 

   if(m == 0){
      return nums2
   }  

    for(let i=m; i<m+n;  i++){        
              nums1[i] =nums2[i-m   ]
    }
    return  nums1.sort((a,b)=>a-b)
};


console.log(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3));
