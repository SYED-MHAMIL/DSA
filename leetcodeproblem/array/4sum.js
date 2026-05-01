var fourSum = function(nums, target) {
    // sorted
    //  
      nums.sort((a,b)=>a-b) 
    let res =  [] 
     for(let i=0; i< nums.length -3; i++ ){

          
             if(i > 0 &&  nums[i-1] == nums[i]){
                  continue
             }

             for(let j=i+1; j < nums.length-2 ; j++){
                    if(j > i+1 &&  nums[j-1] == nums[j]){
                       continue
                    }
                   let left = j+1 
                   let right = nums.length -1
                   while(left < right){
                        let sum =  nums[i] + nums[j] + nums[left] + nums[right];
                        // console.log(sum,[nums[i] , nums[j] , nums[left], nums[right]]);
                        
                        if(sum === target){
                                res.push([nums[i] , nums[j] , nums[left], nums[right]])
                                while (nums[left +  1]  == nums[left]) {
                                      left++
                                }
                                while (nums[right -  1]  == nums[right]) {
                                      right--
                                }
                                left++
                                right --
                        }else if(sum  < target){
                                left++
                        }else{
                             right--
                        }


                   }

               }
    }
    return res
};

console.log(fourSum([2,2,2,2,2,2],8));
