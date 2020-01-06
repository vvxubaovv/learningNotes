function f_a(){
a=aaa
echo a=${a}
}

echo 1 a=${a} #a=
f_a  #a=aaa
echo 2 a=${a} #a=aaa

#所有方法内的变量与执行环境共享,声明为local的变量不为执行环境共享

function f_b(){
local b=bbb
echo b=${b}
}

echo 1 b=${b} #b=
f_b #b=bbb
echo 2 b=${b} #b=

echo ---------------------

#方法中会修改执行环境中的变量,如果变量重名,会有bug,未共享的使用local声明
a=aaa_aaa
echo 1 a=${a} #a=aaa_aaa
f_a   #a=aaa
echo 2 a=${a} #a=aaa_aaa

b=bbb_bbb
echo 1 b=${b} #b=bbb_bbb
f_b   #b=bbb
echo 2 b=${b} #b=bbb_bbb