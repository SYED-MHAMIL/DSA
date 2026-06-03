/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort((a,b)=> a-b) ; 
    let res =   [ ]

    function subsets(index,nums,current=[]){
        
        // if(index ==  nums.length){
            res.push([...current]);
        //     return;
        // }
        for(let i=index; i<nums.length;  i++){
             if(i > index && nums[i] === nums[i-1]){
                   continue;
             };
                current.push(nums[i]);
               subsets(i+1,nums,current);
       
                //    non take it
                current.pop()
        }   

    }
     subsets(0,nums)
     console.log(res);
     
     return res
};


subsetsWithDup([1,2,2])