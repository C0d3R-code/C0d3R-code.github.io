# Xander Solancho — portfolio

Live website: https://c0d3r-code.github.io/

A responsive static portfolio for Xander Kyle Solancho, a web developer and software engineering student at FEU Tech. No build step or private credentials are required. Open index.html for a local preview, or serve this folder with a static web server.

## Pages

- Home: index.html
- Selected websites and programming projects: work.html
- Kira’s Arts website case study: kirasarts.html
- Website packages from US$499, custom programs from US$50 (larger projects around US$200), and USD-to-PHP estimates: services.html
- About: about.html
- Contact and email draft form: contact.html
- Chat and privacy information: privacy.html

## Integrations

Botpress Webchat is embedded on all pages. Its instructions and knowledge are managed and published in Botpress. Chat does not automatically send an email to Xander. The contact form prepares a draft in the visitor’s email application; it does not submit information to a server.

The calculator uses the public ExchangeRate-API daily USD endpoint and caches a reference in browser local storage until the next update. It falls back to a dated reference rate when offline or unavailable. Visitors can enter a custom rate. PHP values are estimates; published package totals are US$499 for one page, US$999 for two, US$1,499 for three, US$1,999 for four, and US$2,499 for five. Each additional page beyond three adds US$500. Internet access is required for updated rates, web fonts, and live AI chat.

## Project credits

Kira’s Arts screenshots are used to show Xander’s website design and implementation. Artwork and artist branding belong to Kira’s Arts. The case study is labeled as a prototype and does not claim live payment processing or automatic Telegram order delivery.

The projects/ folder contains selected C++, Python, Java, and Arduino source files. The console Snake game uses Windows console headers. The separate OpenGL Snake game uses FreeGLUT, OpenGL, and GLU; build notes are in projects/opengl-snake-README.md. The Arduino sketch requires the SevSeg library.

## Social discussions and payments

- X for project discussions and progress updates: https://x.com/Xander202621
- Payment methods: payments.html
- PayPal destination: https://www.paypal.me/XSolancho
- Original wallet images: assets/gcash-qr.png and assets/maya-qr.png

The PayPal amount helper creates a hosted PayPal.Me link with an optional USD amount. It does not create an order, capture card details, or verify payment. Card funding and guest checkout depend on PayPal account and checkout eligibility. The supplied account is Personal; a dedicated Business card checkout is not configured. Wallet payments use the original supplied QR images and require receipt verification by the owner.

Bank linking and automatic transfers are managed within PayPal, not this static website. Never put bank credentials, card data, API secrets, or a PayPal password in these files.
