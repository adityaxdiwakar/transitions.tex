lines = []
while True:
    line = input()
    if line:
        stripped_line_no_slash = line.strip().strip("\\")
        split_lines_ampersand = stripped_line_no_slash.split("&")
        trimmed_split = [s.strip() for s in split_lines_ampersand]
        lines.append(trimmed_split)
    else: break
print(lines[1:-1])
