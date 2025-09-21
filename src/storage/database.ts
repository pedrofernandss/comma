export interface IStorageService {
    hasBeenSent(link: string): Promise<boolean>;

    saveAsSent(link:string): Promise<void>
}