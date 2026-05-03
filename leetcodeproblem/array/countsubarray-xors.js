// length of subarray equals to  k  


const  lengthSubarray = (arr,k)=>{
    
    let sum = 0 
    let low = 0 
    let high = 0 
    let n= arr.length  
     let count =   0
    while (high <n) {
        sum += arr[high]; //
        if (sum == k ) {
             count++
             high++
        }else if(sum < k){
              high++
        }else{
           while (sum > k) {
                 sum-=arr[low]
                 if (sum  == k ) {
                    count++
                 }
                 low++  
           }
           high++
        } 
         
    }
    return count
}



// console.log(lengthSubarray( [4,2, 2,6,4], k = 6));

// the length of subarray with XOR equals to k
// 1. we will use prefix XOR
// 2. we will use map to store the frequency of prefix XOR  
// 3. we will iterate through the array and calculate the prefix XOR and check if the target XOR (prefix XOR ^ k) is present in the map, if yes then we will add the frequency of target XOR to the count
// 4. we will also store the current prefix XOR in the map with frequency 1 if it is not present or increment the frequency if it is present
// 5. finally we will return the count of subarray with XOR equals to k




// const lengthofSubarrayXor =(arr,k)=>{
//      let  map=new Map();
//      let  xor =  0 
//      let count =0 
//      map.set(0,1)
//      for(let i=0; i< arr.length; i++){
//         xor^= arr[i]
//         let target = xor ^  k
//         if (map.has(target)) {
//              count += map.get(target)
//         }
        
//         // store current XOR
//          map.set(xor,(map.get(xor) || 0 ) + 1)
    
//      }
//      return count
// }


// console.log(lengthofSubarrayXor( [4, 2, 2, 6, 4], k = 6));



// the time complexity is O(n) and space complexity is O(n) because of the map



// find all the subarray with XOR equals to k and return the possible subarray

const findXorEqualSubarray = (arr,k) => {
     //
     const res = []
     let xor =  0
     let map = new Map();
     map.set(0,[-1]); // to handle the case when the prefix XOR itself is equal to k, we need to consider the subarray from the beginning of the array, so we set the prefix XOR 0 at index -1 
     
     for(let i=0; i<arr.length; i++){
          xor^= arr[i];  
          let target = xor ^ k ;

          let prevXorIndices = map.get(target)
          if(map.has(target)){
               for(let prevIndex  of  prevXorIndices){
                    let subarray = arr.slice(prevIndex+ 1,i + 1)
                     res.push(subarray)
               }
               
          }
          if (map.has(xor)) { 
               map.get(xor).push(i)
          }else{
               map.set(xor,[i])
               
          }
     }
     return res
     
}
// here we are storing the index of the prefix XOR in the map instead of frequency because we want to return the subarray with XOR equals to k, so we need the index of the prefix XOR to slice the subarray from the original array. but here is problem if there are multiple prefix XOR with the same value then we will only get the last index of that prefix XOR, so we need to store all the indices of the prefix XOR in the map, so we can get all the subarray with XOR 
// equals to k.


console.log(findXorEqualSubarray([4,2,2,6,4],6));


