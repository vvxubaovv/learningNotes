void main(){
	print("hello world!");
	
	first();
	
	print(second("second"));
	print(third("third"));
	print(forth());
	print(fifth("xubao"));
	
	//可选参数,与其他语言类似,可选参数必须放在后面 k:v 只适合可选参数
	//print(sixth(e:"i",a:"a"));//error
}

void first(){
//数字类型为num 子类型分为int(任意长度的整形) 和double(双精度浮点)
var v1=123;
var v2=1234.0;
//字符串可以用' 和 " 创建 类似python
var v3="12345";
var v4='123456';
print(v1);
print(v2);
print(v3);
//类似占位符输出
print("${v1},${v2},$v3");
print(v1+v2);
//字符串无法连接数字
//print(v3+v1);
//此sdk支持字符串相加,旧版可能不支持
print(v3+"jijij");
//字符串可以通过' '连接 不支持字符串变量连接
print('jjjj'' ''kkkkk');

//断言 如果不为true则程序停止运行,只在检查模式下有效 即 dart -c
assert(v3=='12345');
//assert(v2==123);

//声明原始字符,可以忽略转义字符 前面加r 与python中一样
print("我们\n很好");
print(r"我们\n很好");

//const定义编译时常量(值在编译时就确定) final定义运行时常量
const v5 = "jjjjj";
const v6 = v5;
//报错 只能用编译时常量赋值
//const v7 = v4;
const list1 = const[1,2,3];//ok
const list2 = [1,2,3];//ok 默认使用const
//不能修改
//list2[1]=5;

final v8 = v5;
final v9 = v4;

final list3 = [1,2,3];//ok
list3[1]=5;//ok 跟java中的final类似
final list4 = const[1,2,3];//ok
//final list5 = const[new DateTime.now(),2,3];//error
//不能同时有const var 或final var
//const var v10 = 3;

}

//函数 返回值类型可以忽略,参数类型可以忽略
second(a){
print(a);
}

third(b){
print(b);
return "return third";
}

final forth = ()=>"return forth";

var fifth = (name)=>"return fifth$name";

var sixth = (e,{a,b:"b",c="c"})=>"return sixth a=$a,b=$b,c=$c,e=$e";

//顺序 类似python args
seventh(a, [b, c=3, d=4, e])
{
  print('$a $b $c $d $e');
}
