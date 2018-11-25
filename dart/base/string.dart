//https://api.dartlang.org/stable/2.0.0/dart-core/String-class.html

void main(){
  string();
  string1();
}

void string(){
  var a = 'aaa';
  print("a=${a}");
  var b = "bbb";
  print("b=${b}");
  //注意开头和结尾换行符
  var c = '''cccc
  ccccc
  cccc
  cc
  ''';
  print("c=${c}end");
}

void string1(){
  //以字符集编码生成字符
  var c = String.fromCharCode(65);
  print("c=${c}");
}
