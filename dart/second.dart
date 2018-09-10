void  main(){
  A a = new A();
  a.a="a";
  a.b=1;
  a.c=a;
  a._d=1.222;
  print(a);
  
  //B b = new B();//error 定义有参构造函数后无参失效
  B b = new B("a","b","c","_d","e");
  b._d = 333;//貌似跟python一样只做表示没有效果
  print(b._d);
  
  C c = new C();
}

//定义类 类似java 如无声明构造函数,则自带默认构造函数
class A{
  var a;
  var b;
  var c;
  //表示私有属性,暂未确定访问范围
  var _d;
}
//与java类似,是单继承
class B extends A{
  var e;
  //this.xx赋值貌似只允许本类中定义的变量,父类继承不行
  B(a,b,c,_d,this.e){
    this.a = a;
    this.b = b;
    this.c = c;
    this._d = _d;
  }
}

class C{
  C._();
  C(){}
}
