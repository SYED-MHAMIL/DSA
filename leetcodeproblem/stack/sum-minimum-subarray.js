/**
 * @param {number[]} arr
 * @return {number}
 */
function prevSmallernumber(array) {
    let stack = [];
    let result = new Array(array.length).fill(-1);

    for (let i = 0; i < array.length; i++) {
        while (stack.length > 0 && array[stack[stack.length - 1]] >= array[i]) {
            stack.pop();
        }

        if (stack.length > 0) {
            result[i] = stack[stack.length - 1]; // index of previous smaller
        }

        stack.push(i);
    }

    return result;
}

function nextSmallernumber(array) {
    let stack = [];
    let result = new Array(array.length).fill(array.length); // default if no smaller

    for (let i = 0; i < array.length; i++) {
        while (stack.length > 0 && array[stack[stack.length - 1]] >= array[i]) {
            result[stack[stack.length - 1]] = i; // index of next smaller
            stack.pop();
        }
        stack.push(i);
    }

    return result;
}

var sumSubarrayMins = function(array) {
    let pse = prevSmallernumber(array);
    let nse = nextSmallernumber(array);
    console.log([3,1,2,4]);
    
    console.log('pse : ' ,pse);
    console.log('nse : ' ,nse);
    
    let minSumarr = 0;
    let modulo = 1e9 + 7;

    for (let i = 0; i < array.length; i++) {
        let left = i - pse[i];  // count from left
        let right = nse[i] - i; // count from right 
        let  res =   left * right 
        console.log('res',res);
         
        minSumarr = (minSumarr + (left * right * array[i]) % modulo) % modulo;
    } 

    return minSumarr;
};


console.log(sumSubarrayMins([3,1,2,4]));
