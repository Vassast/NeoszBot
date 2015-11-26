import IrcBot
import IrcConnection
import PingHandler
import FrankerZ

f = open('pass.txt')
password = f.read()
f.close()
bot = IrcBot.IrcBot()

whisperCon = IrcConnection.IrcConnection('199.9.253.119', 6667)
whisperCon.login('NeoszBot', password)
whisperCon.sendMessage('CAP REQ :twitch.tv/commands')

channelCon = IrcConnection.IrcConnection('irc.twitch.tv', 6667)
channelCon.login('NeoszBot', password)
channelCon.joinChannel('#neosztv')

bot.addMessageHandler(PingHandler.PingHandler())
bot.addMessageHandler(FrankerZ.FrankerZ())

bot.addConnection(whisperCon)
bot.addConnection(channelCon)

bot.run()