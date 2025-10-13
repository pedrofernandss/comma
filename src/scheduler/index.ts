import rssSources from '../config/article_sources.json';
import { selectRandomSource } from '../content/selector';
import { fetchLatestArticle } from '../content/fetcher';
import { sendWhatsappMessage } from '../whatsapp/index';
import { MssqlStorageService } from '../storage';

export async function runDailyUpdate() {
  try {
    const storageService = new MssqlStorageService();
    const max_attempts = 10;

    for (let i = 0; i < max_attempts; i++) {
      const source = selectRandomSource(rssSources);

      if (!source) {
        console.log('No source selected. Exiting');
        continue;
      }

      const article = await fetchLatestArticle(source);
      if (!article) {
        console.log('No new article found from source. Exiting.');
        continue;
      }

      const isNew = !(await storageService.hasBeenSent(article.link!));

      if (isNew) {
        await sendWhatsappMessage(article!);
        await storageService.saveAsSent(article.link!);
        return;
      } else {
        console.log(`Article "${article.title}" has already been sent. Trying another one...`);
      }
    }
    console.log('Bot finished successfully.');
  } catch (error) {
    console.error(error);
  }
}
