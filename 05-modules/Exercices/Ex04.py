import sys

args = sys.argv
args.pop(0)
args_soma = 0
for arg in args:
    args_soma += int(arg)
args_avg = args_soma / len(args)
print(f"Sum of parameters is {args_soma}, average is {args_avg}")