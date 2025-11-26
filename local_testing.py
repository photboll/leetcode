import ast
import inspect

def parse_line(line):
    line = line.strip()
    if not line:
        return None
    # try python literal first (lists, ints, tuples, dicts, etc.)
    try:
        return ast.literal_eval(line)
    except Exception:
        pass
    # fallback: raw string
    return line

def load_and_parse(path):
    # Opens the file at path and yields each line 
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield parse_line(line)
            
def load_testcases(argcount, *args):
    buf = []
    for parsed in load_and_parse(*args):
        buf.append(parsed)
        if len(buf) == argcount:
            yield buf
            buf.clear()


def run_tests(path, func, max_test=100):
    signature = inspect.signature(func)
    argcount = len(signature.parameters)
    for testcase in load_testcases(argcount, path):
        result = func(*testcase)
        print(result)
        max_test -= 1
        if max_test <= 0:
            return
    
    
        

"""
1. Find the function with leetcode solution. First func on Solution class
2. Find the required arguments
3. read the TEST file line by line trying to parse each line as the described argument


"""