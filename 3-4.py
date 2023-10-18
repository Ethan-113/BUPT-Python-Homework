def queue_out(stack, num):
    pop_out = []

    if num > len(stack):
        for x in range(len(stack)):
            poped = stack.pop(0)
            pop_out.append(poped)
    else:
        for x in range(num):
            poped = stack.pop(0)
            pop_out.append(poped)

    return pop_out

def queue_in(stack, to_push):
    num = len(to_push)
    for x in range(num):
        pushed = to_push[x]
        stack.append(pushed)

def print_stack(stack):
    lenth = len(stack)
    if lenth != 0:
        data = " ".join(map(str, stack))
        print('len = %d, data = %s' % (lenth, data))
    else:
        print('len = 0')

if __name__ == "__main__":
    count = int(input())
    start = input()
    stack_start = [int(x) for x in start.split()]
    pop_finish = []

    for x in range(2):
        directive = input()
        directives = directive.split()

        if directives[0] == 'out':
            pop_now = queue_out(stack_start, int(directives[1]))
            pop_finish = pop_finish + pop_now

        if directives[0] == 'in':
            push_wait = []
            for x in range(len(directives)-1):
                push_wait.append(int(directives[x+1]))
            queue_in(stack_start, push_wait)

    print_stack(stack_start)
    print_stack(pop_finish)