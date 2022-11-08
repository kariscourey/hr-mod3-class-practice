class MyNode {
    constructor(value,
        link=null) {
            this.value = value;
            this.link = link;
        }
}


var a = new MyNode(0);
console.log(a);
console.log(a.value);
console.log(a.link);
a.link = new MyNode(1);
console.log(a.link);
