def parse_input(raw_lines):

    if not raw_lines:
        raise ValueError
    
    if len(raw_lines) != 2:
        raise ValueError
    

    k = 0
    m = 0
    m_array = []

    # parse first line
    first_line = raw_lines[0].strip().split()

    if len(first_line) != 2:
        raise ValueError
    
    k = int(first_line[0])
    m = int(first_line[1])

    if (k < 0 or m < 0):
        raise ValueError

    
    # parse second line
    second_line = raw_lines[1].strip().split()
    if len(second_line) != m:
        raise ValueError
    
    for req in second_line:
        m_array.append(int(req))

    return k, m_array


