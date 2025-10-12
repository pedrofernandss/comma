import { Article } from '@/types/types';

function formatMessage(article: Article): string {
  const body = `*Olá, eu sou o Comma* Aqui está seu artigo de hoje sobre tecnologia 🗞️

*Assunto:* ${article.title || 'N/A'}
    
*Link:* ${article.link || 'N/A'}`;

  return body;
}

export async function sendWhatsappMessage(article: Article): Promise<void> {
  

  const body = formatMessage(article);

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
