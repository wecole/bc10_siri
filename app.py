import datetime


class Journal(object):
	def __init__(self, journal_author=None):
		self.author=journal_author
		self.date_posted=datetime.datetime.now()
		self.journal_dict={}

	def create_journal_entry(self):
		author = str(raw_input('Type your name: '))
		entry_name = str(raw_input('Type the title: '))
		post = str(raw_input('Type your thoughts:\n'))
		self.journal_dict.update({entry_name:{
			"date": self.date_posted.date(),
			"entry": post}})
		return self.journal_dict

journal = Journal()
stop = 'y'
while stop == 'y':
	print (journal.create_journal_entry())
	print ("Entry posted successfully \n")
	stop = raw_input("Do you wish to add posts?(y/n): ").lower()
	