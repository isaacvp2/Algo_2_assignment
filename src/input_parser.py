def parse_input(raw_lines):

    if not raw_lines:
        raise ValueError("nothing in file")
    
    if len(raw_lines) != 2:
        raise ValueError("needs to be 2 lines")
    

    k = 0
    m = 0
    m_array = []

    # parse first line
    first_line = raw_lines[0].strip().split()

    if len(first_line) != 2:
        raise ValueError("first line should only contain m and k")
    
    k = int(first_line[0])
    m = int(first_line[1])

    if (k < 0 or m < 0):
        raise ValueError("can't have negative m or k")

    
    # parse second line
    second_line = raw_lines[1].strip().split()
    if len(second_line) != m:
        raise ValueError("needs to be m number of requests")
    
    for req in second_line:
        m_array.append(int(req))

    return k, m_array


