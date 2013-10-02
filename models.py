import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from dbhandling import Base

class Guest(Base):
	"""Guest Model"""
	__tablename__ = 'guest'
	id = Column(Integer, primary_key=True)
	name = Column(String(70), unique=True)
	email = Column(String(120), unique=True)
	invitename = Column(String(70))
	regdate = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
	count = Column(Integer)
	comments = Column(Text(length=None))
	decision = Column(Text)	
	
	def __init__(self, name, email=None, invitename=None, regdate=None, count=1, decision="Yes", comments=None):
		self.name = name
		self.email = email
		self.invitename = invitename
		self.decision = decision
		self.regdate = datetime.datetime.now()
		print self.decision
		if self.decision == "Yes":
			self.count = 1
			if self.invitename != "":
				self.count = 2
		else:
			self.count = 0
		"""
		if self.decision == "No":
			self.count =  0
		elif self.invitename == "":
			self.count = 1
		else:
			self.count = 1
		"""
		self.comments = comments
		self.decision = decision
	
	def __repr__(self):
		return '<User %r>' % (self.name)

