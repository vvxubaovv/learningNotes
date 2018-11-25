//参考网址:https://api.dartlang.org/stable/2.0.0/dart-math/dart-math-library.html
import "dart:math";

void main(){
  random();
  someConstants();
}

void random(){
  var r=new Random();
  //0~3 不包括3
  print("nextInt=${r.nextInt(3)}");
  print("nextDouble=${r.nextDouble()}");
  print("nextBool=${r.nextBool()}");
}

void someConstants(){
  print("e=${e}");
  print("ln2=${ln2}");
  print("ln10=${ln10}");
  print("log2e=${log2e}");
  print("pi=${pi}");
  
}
