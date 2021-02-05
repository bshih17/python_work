# 8-9 Messages
def show_messages(messages):
	"""This function goes through each message and prints it."""
	for message in messages:
		print(message)

text_messages = ['Please pick up your phone.',
	'Where is the event?', 'When are you going to be here?']

print("8-9 Messages:")
show_messages(text_messages)

# 8-10 Sending Messages
def send_messages(messages, sent_messages):
	"""
	This function goes through each message and prints it.
	Then it puts the message into sent_messages.
	"""
	while messages:
		current_message = messages.pop()
		print(f"Sending message: {current_message}")
		sent_messages.append(current_message)

text_messages = ['Please pick up your phone.',
	'Where is the event?', 'When are you going to be here?']
sent_text_messages = []

print("\n8-10 Sending Messages:")
send_messages(text_messages, sent_text_messages)
print(text_messages)
print(sent_text_messages)

# 8-11 Archived Messages
text_messages = ['Please pick up your phone.',
	'Where is the event?', 'When are you going to be here?']
sent_text_messages = []

print("\n8-11 Archived Messages:")
send_messages(text_messages[:], sent_text_messages)
print(text_messages)
print(sent_text_messages)