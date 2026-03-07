function nextpermutation(arr) {
    let i= arr.length - 2 
    let j= arr.length-1
    let c=arr.length-1
    
    while(i <= 0){
       if(arr[i] < arr[i+1]){
        // first get decrasing ele from right
          let first_dec_el = arr[i]
          for(let k=c; k >=0; k--){
              if(arr[c] > arr[i]){
                  [arr[i],arr[c]]=[arr[c],arr[i]]
                  if (arr[arr.length -2] <arr[arr.length -1]) {
                    
                  }
              }
          }
          


       }
    }


}