function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
  var max = Number.MIN_SAFE_INTEGER;
  var memo = {};
  function helper(node) {
    if (!node) {
      return 0;
    }
    var left = helper(node.left);
    var right = helper(node.right);
    max = Math.max(
      max,
      left + node.val + right,
      node.val,
      node.val + left,
      node.val + right
    );
    return Math.max(left + node.val, right + node.val, node.val);
  }
  helper(root);
  return max;
};