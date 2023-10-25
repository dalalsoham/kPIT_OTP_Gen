const nodemailer = require('nodemailer');
const twilio = require('twilio');
const readline = require('readline');
const randomstring = require('randomstring');

// Function to generate a random code
function generateRandomCode() {
  return randomstring.generate(6);
}

// Generate a random code
const randomCode = generateRandomCode();

// Split the random code into two parts
const firstPart = randomCode.slice(0, 3);
const secondPart = randomCode.slice(3);

// Your email credentials and Twilio credentials
const senderEmail = 'arijeetdas001@gmail.com';
const senderPassword = 'csts whga mkti lyxp';
const recipientEmail = 'arijeetdashotmail@gmail.com';
const twilioAccountSid = 'AC14bf1e53e20c5a64cd0dc790c14ec94b';
const twilioAuthToken = '267ce793e1ade29fc5c90392913b3cef';
const twilioPhoneNumber = '+12055649437';
const recipientPhoneNumber = '+917364046052';  // Replace with the recipient's phone number

// SMTP server settings
const smtpTransport = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: senderEmail,
    pass: senderPassword
  }
});

// Send an email with the first part of the code
const emailOptions = {
  from: senderEmail,
  to: recipientEmail,
  subject: 'Random Code Generated',
  text: `Random Code: ${firstPart}`
};

smtpTransport.sendMail(emailOptions, (error, info) => {
  if (error) {
    console.log('Error sending email:', error);
  } else {
    console.log('Email sent to', recipientEmail);
  }
});

// Use Twilio to send the second part as an OTP to the phone number
const twilioClient = twilio(twilioAccountSid, twilioAuthToken);

twilioClient.messages.create({
  to: recipientPhoneNumber,
  from: twilioPhoneNumber,
  body: `Your OTP is: ${secondPart}`
})
  .then(message => {
    console.log('OTP sent to', recipientPhoneNumber);
  })
  .catch(error => {
    console.log('Error sending OTP:', error);
  });

// Set the start time
const startTime = Date.now();

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Main loop
(function checkCode() {
  const currentTime = Date.now();

  // Calculate remaining time
  const remainingTime = 60000 - (currentTime - startTime);
  if (remainingTime <= 0) {
    console.log('Time limit exceeded. Program terminated.');
    rl.close();
    return;
  }

  // Prompt the user for input
  rl.question(`Enter the 6-character alphanumeric code (Time remaining: ${Math.floor(remainingTime / 1000)} seconds): `, userInput => {
    if (userInput === randomCode) {
      console.log('Code matched');
      rl.close();
    } else {
      console.log('Code mismatch');
      checkCode(); // Ask for input again
    }
  });
})();

// Print the original random code
console.log('Original Random Code:', randomCode);