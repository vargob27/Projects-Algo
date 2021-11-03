class Node {
    constructor(value) {
        this.val = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
    }

    addToFront(val) {
        var newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
    }

    removeFront() {
        if (this.head == null) {
            return this.head;
        }
        let removed = this.head;
        this.head = removed.next;
        removed.next = null;
        return this.head;
    }

    front() {
        if (this.head == null) {
            return this.head;
        }
        return this.head.val;
    }
}

var mySLL = new SinglyLinkedList();
mySLL.addToFront(5);
mySLL.addToFront(69);
console.log(mySLL);
console.log(mySLL.removeFront());
console.log(mySLL);
console.log(mySLL.front());
