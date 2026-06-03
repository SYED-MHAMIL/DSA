/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
     let res=  []
     function sumCombination(index,candidates,current=[],target,sum=0){
         if(index == candidates.length){
              if(sum  == target){
                   res.push([...current])
                   console.log(current);
                    
                 
              }
              return     
         }

            let ele = candidates[index]; 
            sum+=ele
            current.push(ele);
            if(sum <= target){
                  sumCombination(index,candidates,current,target,sum)
            }
            
            sum-=ele 
            current.pop();
            sumCombination(index+1,candidates,current,target,sum) 

     }
     sumCombination(0,candidates,current=[],target)
     return res
};

combinationSum([2,3,6,7],7)