/**
 * @param {number[]} arr
 * @returns {number[][]}
 */
class Solution {
    permuteDist(arr) {
        // code here
         let res = [] 
         function permutation(res,freq={},current=[],arr){
             if(current.length == arr.length){

                 
                  res.push([...current])
                  return ;    
             }
             for(let i=0;  i< arr.length; i++){
                 if(!freq[i]){
                    current.push(arr[i])
                    freq[i] = true
                    permutation(res,freq,current,arr);
                    freq[i] = false
                    current.pop()
                 }
             }
                
         }
         permutation(res,{},[],arr)
         return res
    }
}
const obj = new Solution()
console.log(obj.permuteDist([1,2,3]))   







