#!/bin/sh
# SessionEnd: kill the chrome-devtools-mcp CLI daemon and the headless Chrome it spawns.
# They outlive sessions and burn CPU. The CLI restarts the daemon on next use.
pkill -f 'chrome-devtools-mcp/build/src/daemon' 2>/dev/null
pkill -f 'puppeteer_dev_chrome_profile' 2>/dev/null
exit 0
