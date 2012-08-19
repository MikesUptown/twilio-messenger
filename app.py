import os
import csv
from pprint import pprint
from twilio.rest import TwilioRestClient


def run():

	try:
		
		input_file = open("contacts2.csv", "r+")
		contacts = csv.DictReader(input_file)

	except:
		raise

	data = dict()

	for contact in contacts:
		data[contact['First Name'] + " " + contact['Last Name']] = contact['Mobile Phone']
		
	print "Contacts Successfully Parsed!"

	#pprint(data)

	client = twilio_init()

	for name, tel in sorted(data.iteritems()):
		print "Sending SMS to: " + name
		send_sms(client, tel, "Hello Twilio")


def twilio_init():
	
	account_sid = "AC2d8ea1f7406eae5fe9a2ce1ecd37da13"
	auth_token = "641ba3badc482f8fec31901015783bb9"
	client = TwilioRestClient(account_sid, auth_token)

	return client
 
	
def send_sms(client, recipient, msg):

	message = client.sms.messages.create(to=recipient, from_="+442033224154", body=msg)



if __name__=="__main__":
	run()
