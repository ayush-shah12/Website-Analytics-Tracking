# 🌐 Personal Website Visitor Tracker

This is a **lightweight**, privacy-conscious FastAPI backend service designed to **log public request metadata** when users visit your personal website. It uses **publicly available information** such as *public* IP and browser headers — no instrumentation, tracking scripts, or invasive analytics.
This was made for me to analyze the sources of traffic (or lack thereof) to my website.

> ⚠️ No Personally Identifiable Information (PII) is stored, tracked, or cross-referenced. This is purely for personal insight and debugging purposes.

---
![image](https://github.com/user-attachments/assets/6db97e4c-00c6-45df-8838-cb7c06102e51)

## 🔧 Features

- Logs request metadata in Logfire as well as sending real-time email alerts. 
- Extracts general geolocation info from the *public* IP (e.g., city, country)
- Supports custom source tracking via query params (e.g., `?a=resume` — use a lookup table as I did to obfuscate this if you want too)
- Built with **FastAPI** and designed to work with **any website**! Just add a simple script to call this backend service route on the a user visit to your site. 
- Zero tracking scripts, no cookies or information beyond what the browser already sends and is publically available. 
