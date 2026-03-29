/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {

    let result = new Array(nums1.length).fill(-1)
    let stack = []
    let nums1Idx = {}
   for (let index = 0; index < nums1.length; index++) {
    const element = nums1[index];
           nums1Idx[element] = index
    
   }
   console.log(nums1Idx);
   

    for(let i=0;  i< nums2.length; i++){
        let curr = nums2[i]
        while(stack.length >  0 &&  stack[stack.length -1] < curr ){
                let element  =  stack.pop()
                let idx =  nums1Idx[element]
                result[idx] = curr

        }
        // is this nmber is exits in num1
        // console.log(curr);
        
        if (nums1Idx[curr] !== undefined) {
            console.log(nums1Idx[curr]);            
            stack.push(curr)
        }
        
}
        return result
}

console.log(nextGreaterElement(nums1 = [2,4], nums2 =[1,2,3,4])); // 4,2,1