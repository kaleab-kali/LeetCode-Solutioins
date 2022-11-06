/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let sum = 0
  let j = mat[0].length - 1

  mat.forEach((row, i) => {
    if(i !== j - i)
      sum += row[j - i]
    sum += row[i]
  })

  return sum
};