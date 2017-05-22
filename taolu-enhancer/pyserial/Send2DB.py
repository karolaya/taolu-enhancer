class sDB(object):
	"""docstring for sDB"""
	def __init__(self, arg):
		super(sDB, self).__init__()
		self.arg = arg
		
	def jointsLst(cmm):
	    cmm_s = cmm.split(";")
	    del cmm_s[-1]

	    lst = ["form"]
	    i = 0

	    for i in range(len(cmm_s)):
	        lst.append(cmm_s[i])

	    return(lst)