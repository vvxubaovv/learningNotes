import "dart:math";

void main(){
  var count = 10000000;
  var l = new List();
  var s = new Set();
  var r = new Random();
  for(int i = 10000;i<count;i++){
    var x = r.nextInt(count);
    var y = "${i+x}";
    l.add(y);
    s.add(y);
  }

contains(l,l);
contains(s,l);
  // print(l.contains(40));
  // print(s.contains(40));
}

void contains(coll,test){
  var old=DateTime.now();
  print(old);
  test.forEach((data) => 1+1);//print("${data}:${coll.contains(data)}"));
  var n = DateTime.now();
  print(n);
  print(n.millisecondsSinceEpoch-old.millisecondsSinceEpoch);
}
