import asyncio
import os
from urllib import parse
from pyppeteer import launch

DOWNLOAD_FOLDER = os.getcwd()


async def open_carbonnowsh(url):
    browser = await launch(defaultViewPort=None,
                           handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False,
                           headless=True,
                           args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': DOWNLOAD_FOLDER
    })
    await page.goto(url, timeout=100000)
    return browser, page


async def get_response(url, path):
    browser, page = await open_carbonnowsh(url)
    element = await page.querySelector("#export-container  .container-bg")
    img = await element.screenshot({'path': path})
    await browser.close()
    return (path)
