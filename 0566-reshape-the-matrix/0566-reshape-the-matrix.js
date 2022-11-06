/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    var arr = mat.flat();
  if (r * c != arr.length) return mat;

  var res = [];
  while (arr.length) res.push(arr.splice(0, c));
  return res;
};