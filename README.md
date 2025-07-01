# 🌐 Personal Website Visitor & Icon Analytics

This is a **lightweight**, privacy-conscious FastAPI backend service designed to **log public request metadata** when users visit and interact with your personal website. It uses **publicly available information** such as *public* IP and browser headers — no instrumentation, tracking scripts, or invasive analytics.
This was made for me to analyze the sources of traffic (or lack thereof) to my website.

> ⚠️ No Personally Identifiable Information (PII) is stored, tracked, or cross-referenced. This is purely for personal insight and debugging purposes.

---
<p align="center">
  <img src="https://github.com/user-attachments/assets/f654ce3f-72cb-468b-9d66-c930bbb93ca1" alt="IMG_9531-portrait" />
</p>


## 🔧 Features

- Logs request metadata in Logfire as well as sending real-time email alerts. 
- Extracts general geolocation info from the *public* IP (e.g., city, country)
- Supports custom source tracking via query params (e.g., `?a=resume` — use a lookup table as I did to obfuscate this if you want too)
- Tracks icon clicks on your website to provide insight on user interactions beyond simple page visits. See if someone visited your LinkedIn, GitHub, etc... from your site!
- Built with **FastAPI** and designed to work with **any website**! Just add a simple script to call this backend service route on the a user visit to your site. 
- Zero tracking scripts, no cookies or information beyond what the browser already sends and is publically available. 
