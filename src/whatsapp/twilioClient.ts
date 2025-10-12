import twilio from 'twilio';

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;

if (!accountSid || !authToken) {
throw new Error("TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be configured in the .env file.");
}

const client = twilio(accountSid, authToken);

export default client;