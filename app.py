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

	def delete_entry(self):
		entry = raw_input("input name of post to delete: ")
   		journal_dict.pop(entry)
   		return journal_dict

   	def list_of_entries(self):
	    entries = journal.keys()
	    for item in entries:
	    	print "NAME: {}\n".format(item)
	    	print "DATE: {}\n".format(self.journal_dict[item]["date"])
	    	print "{}\n".format(self.journal_dict[item]["entry"])

	def view_one_journal_entry(self):
		name = raw_input("input name of post to view: ")
		view = self.journal_dict.get(name, None)
		print "NAME: {}\n".format(view)
		print "DATE: {}\n".format(self.journal_dict[view]["date"])
		print "{}\n".format(self.journal_dict[view]["entry"])

1
journal = Journal()
stop = 'y'
while stop == 'y':
	create = raw_input("To create input 1\nTo view posts input 2\nTo delete a post input 3\nTo view one post input 4\n")
	if create == 1:
		print (journal.create_journal_entry())
		print ("Entry posted successfully \n")
	if create == 2:
		journal.list_of_entries()
	if create == 3:
		journal.delete_entry()
	if create == 4:
		journal.view_one_journal_entry()
	stop = raw_input("Do you wish to continue?(y/n): ").lower()
	