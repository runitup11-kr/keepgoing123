


def prt_elements(*args):
    last_index = len(args) -1
    msg = "[ "
    
    for idx, val in enumerate(args):
        msg += str(val) + "," if idx != last_index else str(val)
    msg += " ]"
    
    print(msg)