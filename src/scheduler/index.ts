import rssSources from './config/article_sources.json';
import { selectRandomSource } from './content/selector';
import { fetchLatestArticle } from './content/fetcher';
import { sendWhatsappMessage } from './whatsapp/index';
import { MssqlStorageService } from '@/storage';

export async function runDailyUpdate() {
  try {
    const storageService = new MssqlStorageService();

    const source = selectRandomSource(rssSources);

    if (!source) {
      console.log('No source selected. Exiting');
      return;
    }

    const article = await fetchLatestArticle(source);
    if (!article) {
      console.log('No new article found from source. Exiting.');
    }

    if(await storageService.hasBeenSent(article.link!)) {
      
    } else {
      await storageService.saveAsSent(article.link)
      await sendWhatsappMessage(article!);
    }

    

    console.log('Bot finished successfully.');
  } catch (error) {
    console.error(error);
  }
}
