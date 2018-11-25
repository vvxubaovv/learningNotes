import "dart:io";
import "dart:convert";


void fun1(){
  var dir = Directory("z://a");
  //已经存在没有反应
  var result=dir.createSync();
  print(result);
  print(dir.absolute.path);
  print("fun1 end");
}

void fun2(){
  var dir = Directory("z://b");
  dir.create().then(
    (dir)=>print(dir.absolute.path)
  );
  print("fun2 end");
}

fun3() async {
  var directory = await new Directory("z://c").create();
  print(directory.absolute.path);
}

fun4() async {
  //未创建父路径抱错
  var directory = await new Directory("z://xxx/f").create();
  print(directory.absolute.path);
}

create_file() async{
  var file = File("z://x.txt");
  var e = await file.exists();
  if(e){
    print("已经存在:${file.absolute.path}");
  }else{
    print("还不存在:${file.absolute.path}");
  }
  //已经存在无反应
  file.createSync();
  
  file.writeAsString("我就是xb");
  file.writeAsBytes(UTF8.encode("我还是xb"));
  
  List<String> lins = await file.readAsLines();
  lins.forEach((line)=>print(line));
  
  print("create_file end");
}

void main(){
  fun1();
  fun2();
  fun3();
  
  create_file();
}
