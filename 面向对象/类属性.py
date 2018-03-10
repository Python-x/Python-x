class Tool(object):
	count = 0
	def __init__(self,name):
		self.name = name
		Tool.count += 1
	@classmethod
	def tool_show_count(cls):
		print("创建了%d"%cls.count)
		print("创建了%d"%Tool.count)
ban_shou = Tool("扳手")
gai_zhui = Tool("改锥")
#print(Tool.count)
#print(gai_zhui.count)
#print(ban_shou.count)
Tool.tool_show_count()
