import twilio from 'twilio';

interface Article {
  title?: string;
  link?: string;
  summary?: string;
}

export async function sendWhatsappMessage(article: Article): Promise<void> {
  const accountSid = process.env.TWILIO_ACCOUNT_SID;
  const authToken = process.env.TWILIO_AUTH_TOKEN;
  const from = process.env.TWILIO_FROM_NUMBER;
  const to = process.env.MY_PERSONAL_NUMBER;

  if (!accountSid || !authToken || !from || !to) {
    console.error('Erro: As variáveis de ambiente da Twilio não estão configuradas corretamente.');
    return;
  }

  const client = twilio(accountSid, authToken);

  const body = `*Olá, eu sou o Comma* 

    Aqui está seu artigo de hoje sobre tecnologia 🗞️

    *Assunto:* ${article.title || 'N/A'}
    
    *Link:* ${article.link || 'N/A'}`;

  try {
    const message = await client.messages.create({
      from: `whatsapp:${from}`,
      to: `whatsapp:${to}`,
      body: body,
    });
    console.log(`Mensagem enviada com sucesso! SID: ${message.sid}`);
  } catch (error) {
    console.error('Erro ao enviar a mensagem via Twilio:', error);
  }
}
