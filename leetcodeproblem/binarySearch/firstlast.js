var searchRange = function(nums, target) {
    let first=-1
    let last= -1
    
    let flow = 0
    let fhigh = nums.length -1;
    
    while(flow <= fhigh){
        let fmid = Math.floor((flow+ fhigh)/2);
        if(nums[fmid] == target){
            first = fmid
            fhigh = fmid -1
        }else if(nums[fmid] > target){
             fhigh = fmid -1
        }else{
           flow = fmid+ 1
        }
    }


    let llow = 0
    let lhigh = nums.length -1;
    
    while(llow <= lhigh){
        let lmid = Math.floor((llow+ lhigh)/2);
        if(nums[lmid] == target){
            last = lmid
            llow = lmid+1
        }else if(nums[lmid] > target){
             lhigh = lmid -1
        }else{
           llow = lmid+ 1
        }
    }
    return [first,last]
};


console.log(searchRange([5,7,7,8,8,10],8));
