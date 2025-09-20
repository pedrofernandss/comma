import Parser from 'rss-parser';
import { fetchLatestArticle } from '@/content';

jest.mock('rss-parser');

describe('Article Fetcher', () => {
    beforeEach(() => {
        (Parser as jest.Mock).mockClear();
    });

    it('Should fetch and parse the latest article from a feed URL', async () => {
        const mockFeed = {
            items: [
                {title: 'Most recent article', link: 'http://example.com/post1'},
                { title: 'Oldest article', link: 'http://example.com/post2' }],
        };

        (Parser as jest.Mock).mockImplementation(() => {
            return {
                parseURL: jest.fn().mockResolvedValue(mockFeed)
            }
        })

        const article = await fetchLatestArticle('http://random-url.com/rss');

        expect(article).toBeDefined();
        expect(article?.title).toBe('Most recent article');
        expect(article?.link).toBe('http://example.com/post1')
    });

    it('Should extract a summary from the "content" field', async () => {
        const mockFeedWithContent = {
            items: [
                {
                    title: 'Article with content',
                    link: 'http://example.com/post-content',
                    content: 'This is the summary extracted from content field'
                },
            ],
        };

        (Parser as jest.Mock).mockImplementation(() => {
            return {
                parseURL: jest.fn().mockResolvedValue(mockFeedWithContent),
            };
        });

        const article = await fetchLatestArticle('http://feed-with-content.com/rss');
        expect(article?.summary).toBe('This is the summary extracted from content field')
    });
});