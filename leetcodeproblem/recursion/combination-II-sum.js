//  //  poblem is that can  aslo get the duplicate 

// // Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.Each number in candidates may only be used once in the combination.Note: The solution set must not contain duplicate combinations.

 

// // Example 1:

// // Open in CS Visualizer ▾
// // Input: candidates = [10,1,2,7,6,1,5], target = 8
// // Output: 
// // [
// // [1,1,6],
// // [1,2,5],
// // [1,7],
// // [2,6]
// // ]



function  combination(candidates,target) {
    let res = [] 
    candidates.sort((a,b)=> a-b)
    // [1,1,2,5,6,7,20] TARGET = 8 
    // [1,1,2]  tareget = 3
         
    function sumCombination(index,candidates,target,current,sum) {
        
        if (sum  === target) {
             res.push([...current]);
             return ;
        }
         
        if (sum > target) {
             return ;
        }

        for (let i = index; i < candidates.length; i++) {
             if (i > index  &&  candidates[i] == candidates[i-1]) {
                  continue;
             }

            current.push(candidates[i]);
            sum+= candidates[i]; 
            sumCombination(i+1,candidates,target,current,sum)
            
            // no take it
            sum-=candidates[i];
            current.pop() 
        }
        

    }
    sumCombination(0,candidates,target,[],0)    
    return res
}
// [1,1,2]
console.log(combination(candidates = [1,2,1,1,2,2,2], target = 3))