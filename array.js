let arr=[2,7,11,15]

function twosum(arr,target =6)
{
// convert to sorted array in a way the order of the indexes are preserved
        // let sortedArr = arr.sort((a,b) => a-b)
        let result = []
        for(let i=0; i<arr.length; i++){
            result.push([i,arr[i]])
        }
        result =result.sort((a,b) => a[1] - b[1])
         console.log('result' , result);
         


        let left = 0 
        let right =  result.length -1
        //  1,2,3,4
        //  4,1,0,2
        
        while (left < right) {
            let res = result[left][1] + result[right][1]
            if (res == target) {
            return [
                Math.min(result[left][0],result[right][0]),
                Math.max(result[left][0],result[right][0])
            ]
                
            } else if(res > target){
                right -=1
            }else{
            left+=1
            }
        }
        return []
    }

console.log(twosum(arr));
