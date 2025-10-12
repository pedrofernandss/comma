import rssSources from './config/article_sources.json';
import { selectRandomSource } from './content/selector';
import { fetchLatestArticle } from './content/fetcher';
import { sendWhatsappMessage } from './whatsapp/index';

export async function runDailyUpdate() {
  try {
    const source = selectRandomSource(rssSources);

    if (!source) {
      console.log('No source selected. Exiting');
      return;
    }

    const article = await fetchLatestArticle(source);
    if (!article) {
      console.log('No new article found from source. Exiting.');
    }

    await sendWhatsappMessage(article!);

    console.log('Bot finished successfully.');
  } catch (error) {
    console.error(error);
  }
}
