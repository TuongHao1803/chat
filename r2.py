# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換檔案
def convert(lines):
	person = None
	andy_word_count = 0
	tom_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Andy':
			for m in s[2:]:
				andy_word_count += len(m)
		elif name == 'Tom':
			for m in s[2:]:
				tom_word_count += len(m)
	print('andy說了', andy_word_count, '個字')
	print('tom說了', tom_word_count, '個字')	
		# print(s)


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

# 主要功能
def main():
	lines = read_file('tom.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
















