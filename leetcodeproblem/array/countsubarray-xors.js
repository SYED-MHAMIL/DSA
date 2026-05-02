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



// console.log(lengthSubarray( [4, 2, 2, 6, 4], k = 6));
const lengthofSubarrayXor =(arr,k)=>{
     let  map=new Map();
     let  xor =  0 
     let count =0 
     map.set(0,1)
     for(let i=0; i< arr.length; i++){
        xor^= arr[i]
        let target = xor ^  k
        if (map.has(target)) {
             count += map.get(target)
        }
        
        // store current XOR
         map.set(xor,(map.get(xor) || 0 ) + 1)
    
     }
     return count
}


console.log(lengthofSubarrayXor( [4, 2, 2, 6, 4], k = 6));
    