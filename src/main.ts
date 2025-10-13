import * as dotenv from 'dotenv';
dotenv.config();

import { runDailyUpdate } from './scheduler/index';

runDailyUpdate()
