def lst_cmds(N):
    lst = []
    
    for i in range(N):
        commands = input().split()
        
        cmd = commands[0]
        args = commands[1:]

        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("lst." + cmd)
        else:
            print(lst)
        
if __name__ == '__main__':
    N = int(input()) # number of commands
    lst_cmds(N)
