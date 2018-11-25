import os
import re

def kill_task(pid):
    __windows_kill(pid)
    
def __windows_kill(pid):
    os.system('taskkill /F /PID '+str(pid))
    
def find_java_process(name_pattern):
    resu_list = cmd_excute_wait_result('jps')
    matched_list = __java_match(resu_list,name_pattern)
    pid_dict=__java_pid_find(matched_list)
    return pid_dict
    
def simple_find_java_process(include):
    if include==None or include=='':
        return list()
    reg=r'.*?'+include+'.*'
    p=re.compile(reg)
    pid_dict=find_java_process(p)
    return pid_dict
    
def __java_match(resu_list,name_pat):
    matched_list = list()
    for resu in resu_list:
        #除去pid 只匹配名称
        index = resu.index(' ')
        resu_tmp=resu[index+1:]
        print("resu_tmp:"+resu_tmp)
        m=name_pat.match(resu_tmp)
        if m!=None:
            matched_list.append(resu)       
    return matched_list
    
p=re.compile(r'(\d+)(.*)')
def __java_pid_find(matched_list):
    pid_dict = dict()
    for matched in matched_list:
        print("matched:"+matched)
        m=p.match(matched)
        if m != None:
            pid_dict[m.group(1)]=m.group(2)[1:]
    print('pid_dict:'+str(pid_dict))
    return pid_dict
    
    
def cmd_excute(cmd):
    return os.popen(cmd)
    
def cmd_excute_wait_result(cmd):
    p=cmd_excute(cmd)
    resu = list()
    line=p.readline()
    while line != "":
        resu.append(line)
        line=p.readline()
    p.close()
    print("resu:"+str(resu))
    return resu
    
if __name__=='__main__':
    #find_java_process(re.compile('.*'))
    pid_dict=simple_find_java_process('Test')
    for k in pid_dict.keys():
        print('kill '+pid_dict.get(k)+'  pid:'+str(k))
        kill_task(k)
