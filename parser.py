#! /usr/bin/python
import sys

#this class must read a file, according to a given rule set in the construtor (say 'csv') 
#and return a dictionary (the key is the i-th column passed in the constructor)
#It must also write a stream into a file (tbd)

class Parser:
	
	#constructor
	def __init__(self):
		print "parser created"		

	#returns a dictionary, with key = column number as primary_key
	#and value = tuple with all other columns
	def ReadToDict(self, file_name, delimiter="", primary_key = 0):
		print "reading " + str(file_name)
		ret_dict = {}
		fin = None
		try:
			fin = open(file_name,'r')
			for line in fin:
				s_arr = line.split(delimiter)
				tup = ()
				cnt = 0
				key = ""
				for s in s_arr: #create a tuple
					val = ""
					if '\n' in s:
						m = s.split('\n')
						if '\r' in m[0]:
							n = m[0].split('\r')
							val = n[0]
						else:
							val = m[0]
					else:
						val = s
					if cnt == primary_key:
						key = val	
					else:
						tup += (val,)
					cnt += 1
				ret_dict[key] = tup
		except:
			print "error in reading file " + str(file_name)
		if fin is not None and not fin.closed:
			print "closing file " + str(file_name)
			fin.close()
		return ret_dict


	#returns a list of tuples, with all columns of the file
	#(columns must be known, before using the tuple)
	def ReadToList(self, file_name, delimiter=""):
		print "reading " + str(file_name)
		ret_list = []
		fin = None
		try:
			fin = open(file_name,'r')
			for line in fin:
				s_arr = line.split(delimiter)
				tup = ()
				for s in s_arr: #create a tuple
					if '\n' in s:
						m = s.split('\n')
						if '\r' in m[0]:
							n = m[0].split('\r')
							tup += (n[0],)
						else:
							tup += (m[0],)
					else:
						tup += (s,)
				ret_list.append(tup)
		except:
			print "error in reading file " + str(file_name)
		if fin is not None and not fin.closed:
			print "closing file " + str(file_name)
			fin.close()
		return ret_list


	def Write(self, file_name, list_stream = []):
		ret = False
		if list_stream is not []:
			fout = None
			try:
				fout = open(file_name,'w')
				for s in list_stream:
					fout.write(s + '\n')				
				ret = True
			except:
				print "error in writng file " + str(file_name)
			if fout is not None and not fout.closed:
				print "closing file" + str(file_name)
				fout.close()
			return ret

