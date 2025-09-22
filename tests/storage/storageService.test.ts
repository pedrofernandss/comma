import { IStorageService } from '@/storage';

class FakeStorageService implements IStorageService { // Simula um serviço de armazenamento
  private sentLinks: string[] = []; //Para guardar os links

  async hasBeenSent(link: string): Promise<boolean> {
    return this.sentLinks.includes(link);
  }

  async saveAsSent(link: string): Promise<void> {
    const alreadySent = await this.hasBeenSent(link);
    
    if (!alreadySent){
      this.sentLinks.push(link);
    }
  }
}

describe('Storage service', () => {
  it('Should return false if a link has not been sent before', async () => {
    const storage = new FakeStorageService();
    const newLink = 'http://example.com/new-article';

    const result = await storage.hasBeenSent(newLink);

    expect(result).toBe(false);
  });

  it('Should not save a duplicate link', async () => {
    const storage = new FakeStorageService();
    const duplicateLink = 'http://example.com/duplicate-article';
    
    await storage.saveAsSent(duplicateLink);

    await storage.saveAsSent(duplicateLink); // Try to save a second time

    const internalLinks = (storage as any).sentLinks;
    expect(internalLinks.length).toBe(1);
  })
});
