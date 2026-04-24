#!/usr/bin/env node
const fs = require("fs");

async function main() {
  const raw = fs.readFileSync(0, "utf8");
  const input = raw.trim() ? JSON.parse(raw) : {};
  const url = input.url;
  const timeout = Number(input.timeout || 20000);
  const limit = Number(input.limit || 200);

  if (!url) {
    throw new Error("playwright_recon.js requires {\"url\": \"...\"} on stdin");
  }

  const { chromium, devices } = require("playwright");
  const browser = await chromium.launch({ channel: "chrome", headless: true });
  const context = await browser.newContext({
    ...devices["Desktop Chrome"],
    locale: "en-US",
  });
  const page = await context.newPage();
  const requests = [];

  page.on("request", (request) => {
    if (requests.length >= limit) {
      return;
    }
    requests.push({
      method: request.method(),
      resourceType: request.resourceType(),
      url: request.url(),
    });
  });

  try {
    await page.goto(url, { waitUntil: "networkidle", timeout });
  } finally {
    await browser.close();
  }

  const interesting = requests.filter((item) =>
    /\/api\/|graphql|\.json(\?|$)/i.test(item.url)
  );
  process.stdout.write(
    JSON.stringify(
      {
        url,
        totalRequests: requests.length,
        interesting,
      },
      null,
      2
    ) + "\n"
  );
}

main().catch((error) => {
  process.stderr.write(String(error && error.stack ? error.stack : error) + "\n");
  process.exit(1);
});
