import { Article } from '@/types/types';
import client from './twilioClient';

export async function sendWhatsappMessage(article: Article): Promise<void> {
  const from = process.env.TWILIO_FROM_NUMBER;
  const recipientsString = process.env.RECIPIENT_NUMBERS;
  const contentSid = process.env.TWILIO_TEMPLATE_SID;

  if (!from || !recipientsString || !contentSid) {
    console.error('Error: Missing environment variables (sender, recipients, or template SID)');
    return;
  }

  const recipients = recipientsString.split(',');

  const sendPromises = recipients.map((recipient) => {
    return client.messages.create({
      from: `whatsapp:${from}`,
      to: `whatsapp:${recipient}`,
      contentSid,
      contentVariables: JSON.stringify({
        '1': article.title || 'Sem título',
        '2': article.link || 'Sem link',
      }),
    });
  });

  try {
    const results = await Promise.all(sendPromises);
    console.log(`Successfully sent ${results.length} messages.`);
  } catch (error) {
    console.error('Error sending one or more messages via Twilio:', error);
  }
}
