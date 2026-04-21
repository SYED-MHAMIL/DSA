/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    // left , right
    // [1,2,3]
    // pivot :find the first samllast from the right side
    // if pivot exits : then again traverse right to elft to get the first grather element
    // and then reverse the suffix of pivot

    let pivot =-1;
    for(let i=nums.length -1;  i>0; i--){
        if(nums[i] > nums[i-1]){
          pivot = i -1
          break
        }
    }

    if(pivot == -1){
             return nums.sort((a,b)=> a-b)
    }
    
    let largest; 
    for(let i=nums.length -1;  i>=0; i--){
        if(nums[i] > nums[pivot]){
          largest= i
          break
        }
    }
     [nums[pivot],nums[largest]] = [nums[largest],nums[pivot]] 
     
    let left = pivot +1
    let right = nums.length -1
    while(left < right){
    [nums[left],nums[right]] = [nums[right],nums[left]]
     left++
     right-- 
      
    }
    return nums

};


console.log(nextPermutation([1,2,3]));
