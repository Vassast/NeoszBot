import MessageHandler

class FrankerZ(MessageHandler.MessageHandler):
	def __init__(self):
		super().__init__()
		
	def update(self, data):
		if data[1] == 'PRIVMSG':
			message = data[2][1].replace('\r\n', '')
			print(message)
			if message == 'FrankerZ':
				self.addMessage(('PRIVMSG', '#neosztv FrankerZ'))
