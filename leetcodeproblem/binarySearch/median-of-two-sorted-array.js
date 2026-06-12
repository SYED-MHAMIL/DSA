    /**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // 
    let n = nums1.length + nums2.length ;
    if(nums1.length  >  nums2.length){
        return  findMedianSortedArrays(nums2,nums1)
    }
    let half  =Math.floor((n+1)/2);
     
    let low = 0;
    let high = nums1.length    

     while(low <= high){
        let i =Math.floor((low + high)/2);
        let j = half - i

        let l1 =  i-1 >= 0   ? nums1[i - 1]  : -Infinity
        let l2 =  j -1 >= 0  ? nums2[j-1] :-Infinity
        let r1 =  i < nums1.length  ? nums1[i] : Infinity
        let r2 = j < nums2.length  ? nums2[j] : Infinity
     
     
        if(l1 <= r2 && l2 <= r1){
             if(n % 2  == 1){
                return Math.max(l1,l2)
             }
             return (Math.max(l1,l2) + Math.min(r1,r2)) / 2
        }else if(l1 > r2){
            high = i -  1
        }else{
            low  = i+1
        }
     
     }


};

console.log(findMedianSortedArrays([1,3,5],[2,4]));
//  you clan alos put the even number