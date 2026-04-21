// brute force


/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    // check previous one if this overlap so merge
  intervals.sort((a,b)=> a[0]-b[0]) 
  let ans = []
  let  i=0
  let n = intervals.length
  while(i<n){
      let start = intervals[i][0]
      let end = intervals[i][1]
      
      let j = i+1
    //   merge overlapping when we needed
    while(j < n && end >= intervals[j][0]){
          end = Math.max(intervals[j][1],end)
         j++
    }
     ans.push([start,end])
     i=j

   }   
  return ans
};