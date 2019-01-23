import itchat

@itchat.msg_register(["Text","Map","Sharing","Picture"])
def text_reply(msg):
	print(msg)
	replay_content = "[自动回复]您好，我现在正忙，一会再做答复。"
	if msg['Type'] == "Text":
		replay_content = "[自动回复]您好，我现在正忙，一会再做答复。已收到您的消息："+msg['Content']
	if msg['Type'] == "Picture":
		replay_content = "[自动回复]您好，我现在正忙，一会再做答复。已收到您的图片"
	itchat.send_msg("收到{}的信息：{}".format(msg["User"]["RemarkName"], msg["Text"]), "filehelper")
	return replay_content

# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
itchat.auto_login()
itchat.run()
