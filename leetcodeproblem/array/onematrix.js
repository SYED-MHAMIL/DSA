// Input:
// matrix = [
// [0,0,0],
// [0,1,0],
// [0,0,0]]

// Output:
// [[0,1,0],[1,1,1],[0,1,0]]

// Explanation:
// Since matrix[1][1] = 1, therefore the 2nd row and 2nd column will be set to 1.

// Input:
// matrix = [[1,0,0,1],[0,0,0,0],[0,0,1,0]]

// Output:
// [[1,1,1,1],[1,0,1,1],[1,1,1,1]]

// Explanation:
// Since matrix[0][0] = 1, matrix[0][3] = 1, and matrix[2][2] = 1,
// therefore corresponding rows and columns will be set to 1.


function oneMatrix(array) {
    let fistRowOne =  false
    let firstColOne = false
    

     let n = array.length;
      let m= array[0].length;
    for (let i = 0; i < n; i++) {
        const element = array[i][0];
        if (element == 1) {
               firstColOne= true
        }
    }


    for (let i = 0; i < m; i++) {
        const element = array[0][i];
        if (element == 1) {
               fistRowOne= true
        }
    }

// marketr
     for (let i = 1; i < n; i++) {
        for (let j = 1;   j < m;   j++) {
            const cel = array[i][j]
            if (cel == 1) {
                array[0][j] = 1
                array[i][0] =1
            }
            
        }
        
     }


     
     for (let i = 1; i < n; i++) {
        for (let   j = 1; j < m;   j++) {
            const col = array[i][0]
            const row = array[0][j]
            if (col == 1 || row ==1) {
                array[i][j] = 1
                
            }
            
        }
        
     }
    


     if (firstColOne) {
        for (let i = 0; i <  n; i++) {
            array[i][0]  =1
            
        }
     }
    
     
     if (fistRowOne) {
        for (let i = 0; i <  m; i++) {
            array[0][i]  =1
            
        }
     }


     return  array
    
}

console.log(oneMatrix(matrix = [[1,0,0,1],[0,0,0,0],[0,0,1,0]]));
