

// Input: arr[] = [2, 3]
// Output: [0, 2, 3, 5]
// Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.


function subsetSums(arr) {
    let res =  []
     function  subsets(index,arr,sum) {
         if (index === arr.length ) {
             res.push(sum) 
               return ;
           }
           
           sum+=arr[index];
           subsets(index+1,arr,sum);

        //    non take it
        
           sum-=arr[index];
           subsets(index+1,arr,sum);

     }
    subsets(0,arr,0);
    res.sort((a,b)=>a-b)
    console.log(res);
    
}

subsetSums([2,3])