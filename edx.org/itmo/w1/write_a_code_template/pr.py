#!python3

with open('input.txt', 'r') as fr:
    w, h = [int(i) for i in fr.readline().strip().split(' ')]
    key_to_coord = {}
    while h > 0:
        h -= 1
        line = fr.readline().strip()
        for i,e in enumerate(line):
            key_to_coord[e] = (h+1, i+1)

    time_min = 9e9
    min_lang = None
    while True:
        line = fr.readline()
        if not line:
            break
        lang_name = line.strip()
        assert(fr.readline().strip() == '%TEMPLATE-START%')
        time = 0
        prev_ch = None
        while True:
            line = fr.readline()
            if not line or line.strip() == '%TEMPLATE-END%':
                break
            for ch in line:
                if ch.isspace():
                    continue
                ch_ij = key_to_coord[ch]
                if prev_ch:
                    prev_ij = key_to_coord[prev_ch]
                    time += max(abs(ch_ij[0]-prev_ij[0]), abs(ch_ij[1] - prev_ij[1]))
                prev_ch = ch
        if time < time_min:
            time_min = time
            min_lang = lang_name
    with open('output.txt', 'w') as fw:
        fw.write("%s\n%d" % (min_lang, time_min))



