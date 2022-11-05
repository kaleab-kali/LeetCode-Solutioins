/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
     // Initialize two pointers p1 and p2 pointing to the head...
    var p1 = head;
    var p2 = head;
    while(p2 != null && p2.next != null){
        // In each iteration, we move p1 one node forward and we move p2 two nodes forward...
        p1 = p1.next;
        p2 = p2.next.next;
    }
    // When p2 reaches the last node, p1 will be exactly at the middle point...
    return p1;
};