def sort(a):
	dic={}
	l=[]
	for i in a:
		dic[''.join(sorted(i))].append(i)
	return sorted(dic.values())
def main():
	a=["nithin","jithin","athul","thaul"]
	print sort(a)
if __name__ == '__main__':
	main()
