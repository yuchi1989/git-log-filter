#!/usr/bin/python3
import sys,os

def matchany(commit, words):
	for word in words:
		if word in commit:
			return True
	return False
def matchall(commit, keywords):
	for keyword in keywords:
			words = keyword.split("||")
			if not matchany(commit, words):
				return False
	return True
def filter(filename1,keywords):
	commits = []
	with open(filename1, encoding = "ISO-8859-1") as tempfile1:
		content = tempfile1.readlines()
		total_line = len(content)
		commit = ""
		flag = False
		for i in range(total_line):
			if i+2 >= total_line:
				break
			if "commit" in content[i] and "Author" in content[i+1] and "Date" in content[i+2]:
				flag = True
				if commit != "":
					commits.append(commit)
				commit = content[i]

			else:
				if flag:
					commit = commit + content[i]
				i = i + 1
		commit = commit + content[total_line-2]
		commit = commit + content[total_line-1]
		commits.append(commit)
	print("Total commits: " + str(len(commits)))
	if keywords != []:
		for keyword in keywords:
			print(keyword)
	finalcommits = []
	for commit in commits:
		if matchall(commit, keywords):
			finalcommits.append(commit)
	print("Total final commits: " + str(len(finalcommits)))
	for commit in finalcommits:
		print(commit)
				


	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print ("input error")
		print ("python3 gitlogfilter.py git_log_file")
		sys.exit(2)
	
	filter(sys.argv[1],sys.argv[2:])
	