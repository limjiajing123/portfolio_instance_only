const axios = require("axios");

// Cooldown state stored here
let lastDiscordAlert = 0;
const DISCORD_ALERT_COOLDOWN_MS = 5 * 60 * 1000; // 5 minutes

async function sendDiscordAlert(error, userMessage) {
    console.log("🚨 sendDiscordAlert CALLED with:", {
        hasError: !!error,
        userMessage,
        webhookPresent: !!process.env.DISCORD_WEBHOOK_URL,
    });
    try {
    const webhookUrl = process.env.DISCORD_WEBHOOK_URL;
    if (!webhookUrl) {
      console.warn("DISCORD_WEBHOOK_URL not set, skipping Discord alert");
      return;
    }

    const now = Date.now();

    // Prevent spamming during prolonged outages
    // if (now - lastDiscordAlert < DISCORD_ALERT_COOLDOWN_MS) {
    //   return;
    // }
    lastDiscordAlert = now;

    const status = error?.response?.status || "no response";
    const errMsg = error?.message || "Unknown error";

    const sgTime = new Date().toLocaleString("en-SG", {
      timeZone: "Asia/Singapore",
      hour12: false,
    });

    const content = [
      "⚠️ **OpenRouter API Error on Portfolio Chatbot**",
      `**Time (SGT):** ${sgTime}`,
      `**User message:** ${userMessage || "(not provided)"}`,
      `**Error message:** ${errMsg}`,
      `**HTTP status:** ${status}`,
    ].join("\n");

    await axios.post(webhookUrl, { content });
  } catch (e) {
    console.error("Failed to send Discord alert:", e.message);
  }
}

module.exports = sendDiscordAlert;
