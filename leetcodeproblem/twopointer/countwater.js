function maxArea(heights) {
       let left= 0
       let right = heights.length -1
       let max_area = 0 
       while(left<right){
          let min_val = Math.min(heights[left],heights[right])
          let area_water = (right- left) * min_val
          max_area = Math.max(max_area,area_water) 

          if( min_val== heights[left]){
               left+=1
          }else{
             right-=1
          }

       }   

       return max_area
    }

console.log(maxArea(height = [1,7,2,5,4,7,3,6]));
