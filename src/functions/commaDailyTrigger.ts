import { app, InvocationContext, Timer } from "@azure/functions";
import { runDailyUpdate } from "@/scheduler";

async function dailyTrigger(myTimer: Timer, context: InvocationContext): Promise<void> {
    await runDailyUpdate();
};

app.timer('commaDailyTrigger', {
    schedule: '0 30 15 * * *',
    handler: dailyTrigger
});