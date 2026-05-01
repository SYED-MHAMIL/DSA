/**
 * @param {Number[]} arr
 * @returns {Number}
 */
class Solution {
    maxLength(arr) {
        // code here
        let maxLen = 0
        let firstseen = new Map()
        let sum =0 
        for(let i=0; i < arr.length; i++){
            sum+=arr[i]
            if(sum == 0){
                maxLen= i+ 1
            }else{
                // a;reawdy there
                if(firstseen.has(sum)){
                    maxLen = Math.max(maxLen,i - firstseen.get(sum))
                }else{
                      firstseen.set(sum,i)                    
                }
            }
        }
               
        

        return maxLen
    }
}