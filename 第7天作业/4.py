with open('text.txt', 'r') as file1:
    lines1 = file1.readlines()

with open('text_copy.txt', 'r') as file2:
    lines2 = file2.readlines()

different_lines = []
for i, (line1, line2) in enumerate(zip(lines1, lines2)):
    if line1 != line2:
        different_lines.append(i)

if not different_lines:
    print("两个文件的内容完全相同。")
else:
    print("不同的行编号:")
    print(different_lines)
