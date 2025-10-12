import * as dotenv from 'dotenv';
import { runDailyUpdate } from './scheduler/index';

dotenv.config();

runDailyUpdate()
