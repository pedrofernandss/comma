import { Article } from '@/types/types';
import client from './twilioClient'

function formatMessage(article: Article): string {
  const body = `*Olá, eu sou o Comma* Aqui está seu artigo de hoje sobre tecnologia 🗞️

*Assunto:* ${article.title || 'N/A'}
    
*Link:* ${article.link || 'N/A'}`;

  return body;
}

export async function sendWhatsappMessage(article: Article): Promise<void> {
  const from = process.env.TWILIO_FROM_NUMBER;
  const recipientsString = process.env.RECIPIENT_NUMBERS;

  if (!from || !recipientsString) {
    console.error('Error: Sender or recipient numbers are not configured in .env');
    return;
  }

  const recipients = recipientsString.split(',');
  const body = formatMessage(article);

  const sendPromises = recipients.map((recipient) => {
    return client.messages.create({
      from: `whatsapp:${from}`,
      to: `whatsapp:${recipient}`,
      body: body,
    });
  });

  try {
    const results = await Promise.all(sendPromises);
    console.log(`Successfully sent ${results.length} messages.`);
  } catch (error) {
    console.error('Error sending one or more messages via Twilio:', error);
  }
