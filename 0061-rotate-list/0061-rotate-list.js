/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {

    if(!head) return null

    let first = head;

    let count = 1;

    while(first.next){

        first = first.next;
        count++;

    }

    first.next = head;

    k = k%count // incase k is grater than n

    let newTail = head;

    for(let i = 0; i<count-k-1; i++){

       newTail = newTail.next;

    }

    head = newTail.next;
    newTail.next = null;

    return head
};