function printSubsequence(index, current, arr) {
    // Base case
    if (index === arr.length) {
        console.log(current);
        return;
    }

    // Include current element [PICK CURRENT]
    current.push(arr[index]);
    printSubsequence(index + 1, current, arr);

    // Backtrack
    current.pop();

    // Exclude current element [SKIP CURRENT]
    printSubsequence(index + 1, current, arr);
}

// Example
let arr = [1, 2, 3];

// printSubsequence(0, [], arr);

// how its working ?

// The function `printSubsequence` generates all possible subsequences of the given array `arr` using recursion.

// 1. The function takes three parameters: `index` (the current index in the array), `current` (the current subsequence being built), and `arr` (the original array).

// 2. The base case is when `index` is equal to the length of the array, which means we have processed all elements. At this point, we print the current subsequence and return.

// 3. The function first includes the current element (at `index`) in the `current` subsequence and makes a recursive call to process the next index.

// 4. After the recursive call returns, it backtracks by removing the last element from `current` (the one that was just included).

// 5. Then, it makes another recursive call to process the next index without including the current element, effectively skipping it.




function allSubsequences(index, current=[], arr){
     if (index  == arr.length) {
          console.log(current);
          return ;
     }

     
     
     current.push(arr[index]);
     //  PICKED
     allSubsequences(index+1,current,arr);
     
     //  NOT PICKED [BACK TARCK]
     current.pop(arr[index]);
     allSubsequences(index+1,current,arr)
    
    
}

// allSubsequences(0,[],[3,2,1])




// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            //     ALL SUBSEQUESNCES WHOSE SUM IS TARGET
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



function allSubsequencesSum(index,arr,current,target,sum) {
        if (index === arr.length) {
              if (sum == target) {
                   console.log(current);
               }     
               return;
        }
        current.push(arr[index])
        // sum+= arr[index]
        allSubsequencesSum(index+1,arr,current,target,sum)

        current.pop();
        sum-= arr[index]
        allSubsequencesSum(index+1,arr,current,target,sum)


}

// allSubsequencesSum(0,[1,1,3],[],1,0)









// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            //     ALL SUBSEQUESNCES WHOSE SUM IS TARGET
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


function oneSubsequencesSum(index,arr,current,target,sum) {
        if (index === arr.length) {
              if (sum == target) {
                        // console.log(current);
                   return 1   
               }     
              return  0
        }
        
        current.push(arr[index])
        sum+= arr[index]
        let l = oneSubsequencesSum(index+1,arr,current,target,sum)
        current.pop();
        sum-= arr[index]
        let r =oneSubsequencesSum(index+1,arr,current,target,sum)

        return l+r;
 
}

console.log(oneSubsequencesSum(0,[1,1,2,3],[],2,0))