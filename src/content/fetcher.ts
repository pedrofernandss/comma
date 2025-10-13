import Parser from 'rss-parser';
import { Article } from '../types/types';

export async function fetchLatestArticle(url: string): Promise<Article | undefined> {
  try {
    const parser = new Parser();
    const feed = await parser.parseURL(url);

    if (!feed.items?.length) {
      return undefined;
    }

    const latestItem = feed.items[0];

    return {
      title: latestItem.title,
      link: latestItem.link,
      summary: latestItem.summary || latestItem.description || latestItem.content || ''
    };
  } catch (error) {
    console.error(`Error to fetch feed from URL: ${url}`, error);
    return undefined;
  }
}
