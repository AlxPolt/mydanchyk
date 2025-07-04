# Adaptive Pickleball Platform (Render Deployment)

This is a real project developed for the Adaptive Pickleball Federation of Ukraine.

## 🚀 Deployment (Render)

1. Create a repository on GitHub and push this code.
2. Go to [https://render.com](https://render.com) and create a new Web Service.
3. Select "Deploy from a GitHub repository".
4. Set environment:
   - Environment: Docker
   - Port: `8000`
5. Confirm and deploy.

## 🔗 Endpoints

- `/` — homepage
- `/courts/` — court list
- `/recommendations?user_id=1` — recommended slots

## 🧠 Tech Stack

- Python 3.11
- FastAPI
- Docker
- Render free tier
