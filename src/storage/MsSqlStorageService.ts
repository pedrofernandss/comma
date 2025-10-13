import sql from 'mssql';
import { IStorageService } from './storageService';

const dbConfig = {
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  server: process.env.DB_HOST || 'localhost',
  database: process.env.DB_DATABASE,
  options: {
    encrypt: true,
    trustServerCertificate: false,
  },
};

export class MssqlStorageService implements IStorageService {
  public async hasBeenSent(link: string): Promise<boolean> {
    try {
      await sql.connect(dbConfig);

      const result = await new sql.Request()
        .input('link', sql.NVarChar, link)
        .query('SELECT COUNT(*) as count FROM sent_articles WHERE link = @link');

      return result.recordset[0].count > 0;
    } catch (err) {
      console.error('Database query error on hasBeenSent: ', err);
      return True;
    } finally {
      await sql.close();
    }
  }

  public async saveAsSent(link: string): Promise<void> {
    const query = `
            INSERT INTO sent_articles (link) VALUES (@link)
        `;

    try {
      await sql.connect(dbConfig);
      await new sql.Request().input('link', sql.NVarChar, link).query(query);
      console.log(`Link saved successfully: ${link}`);
    } catch (err) {
      console.error('Database query error on saveAsSent:', err);
    } finally {
      await sql.close();
    }
  }
}
