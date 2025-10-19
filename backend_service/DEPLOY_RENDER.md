# Deploy to Render (Free)

## Step 1: Prepare Your Repository

1. **Push backend_service to GitHub**:
   ```bash
   # Create a new repo for just the backend service
   cd backend_service
   git init
   git add .
   git commit -m "Initial Star Shell backend"
   
   # Create repo on GitHub and push
   git remote add origin https://github.com/yourusername/star-shell-backend.git
   git push -u origin main
   ```

## Step 2: Deploy on Render

1. **Go to [render.com](https://render.com)** and sign up/login
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repo** (star-shell-backend)
4. **Configure the service**:
   - **Name**: `star-shell-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 30 app:app`
   - **Plan**: `Free` (750 hours/month)

## Step 3: Set Environment Variables

In Render dashboard, go to **Environment** tab and add:

```
GEMINI_KEY_1 = your_first_gemini_api_key_here
GEMINI_KEY_2 = your_second_gemini_api_key_here  
GEMINI_KEY_3 = your_third_gemini_api_key_here
GEMINI_KEY_4 = your_fourth_gemini_api_key_here
GEMINI_KEY_5 = your_fifth_gemini_api_key_here
STAR_SHELL_SECRET = secret-3.14159
```

## Step 4: Deploy

1. **Click "Create Web Service"**
2. **Wait for deployment** (5-10 minutes)
3. **Get your URL**: `https://your-service-name.onrender.com`

## Step 5: Test Your Deployment

```bash
# Test health endpoint
curl https://your-service-name.onrender.com/health

# Should return:
# {"status":"healthy","keys_available":5,"timestamp":"..."}
```

## Step 6: Update Star Shell

Update the backend URL in your Star Shell code:

```python
# In star_shell/main.py, replace:
backend_url = "https://your-service-name.onrender.com"
```

## Important Notes

### Free Tier Limitations:
- **Sleeps after 15 minutes** of inactivity
- **Takes ~30 seconds** to wake up on first request
- **750 hours/month** limit (about 25 days)

### Wake-up Strategy:
The service will sleep but wake up automatically when someone uses the secret option. The first request might be slow (~30 seconds), but subsequent requests will be fast.

### Monitoring:
- Check **Render dashboard** for logs and metrics
- Monitor your **Gemini API usage** in Google Cloud Console
- Set up **billing alerts** to avoid surprises

## Alternative: Railway (No Sleep)

If the sleep issue bothers you, Railway offers $5 free credit monthly with no sleep:

1. Go to [railway.app](https://railway.app)
2. Deploy from GitHub
3. Add environment variables
4. Get ~$5 worth of usage (no sleep issues)

## Cost Comparison:
- **Render Free**: $0/month (with sleep)
- **Railway**: ~$0-5/month (no sleep, pay per usage)
- **Fly.io**: $0/month (small free tier, no sleep)
- **Heroku**: $5/month minimum