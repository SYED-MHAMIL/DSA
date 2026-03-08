function nextpermutation(arr) {
    let i= arr.length - 2 
    let c=arr.length-1
    
    while(i >= 0){
        // first get decrasing ele from right
        if(arr[i] < arr[i+1]){
         console.log(i)
          let first_dec_el = arr[i]
          for(let k=c; k >=0; k--){
                 
              if(arr[k] > arr[i]){                
                  [arr[i],arr[k]]=[arr[k],arr[i]]
                  break
              }
          }
          let l=i+1
          let r= arr.length -1
          while (l < r){
              [arr[r],arr[l]]  = [arr[l],arr[r]] 
              l+=1
              r-=1
          }
          
       return arr
        
       }
       i-=1
    }
    return arr.reverse()

}


console.log(nextpermutation([2,3,1]));
