import datetime
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' const authToken = '1234567899'
const client = require('twilio')(accountSid, authToken)
client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch().then(message= > console.log(“Intruder alert at” + datetime.datetime.now())
