# Deploy to Vercel (Free, No Credit Card)

## ✅ Benefits:
- **Completely free** - no credit card required
- **No sleep** - always responsive
- **Global edge network** - fast worldwide
- **Automatic HTTPS**
- **Easy GitHub integration**

## 🚀 Deployment Steps:

### 1. Push to GitHub
```bash
cd backend_service
git init
git add .
git commit -m "Star Shell Vercel backend"

# Create new repo on GitHub and push
git remote add origin https://github.com/yourusername/star-shell-vercel.git
git push -u origin main
```

### 2. Deploy on Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub (no credit card needed)
3. Click **"New Project"**
4. Import your `star-shell-vercel` repository
5. Click **"Deploy"**

### 3. Add Environment Variables
In Vercel dashboard:
1. Go to your project → **Settings** → **Environment Variables**
2. Add these variables:

```
GEMINI_KEY_1 = your_first_gemini_api_key_here
GEMINI_KEY_2 = your_second_gemini_api_key_here  
GEMINI_KEY_3 = your_third_gemini_api_key_here
GEMINI_KEY_4 = your_fourth_gemini_api_key_here
GEMINI_KEY_5 = your_fifth_gemini_api_key_here
STAR_SHELL_SECRET = secret-3.14159
```

### 4. Redeploy
After adding environment variables, trigger a new deployment:
1. Go to **Deployments** tab
2. Click **"Redeploy"** on the latest deployment

### 5. Test Your Deployment
Your service will be available at: `https://your-project-name.vercel.app`

Test it:
```bash
# Health check
curl https://your-project-name.vercel.app/health

# Should return:
# {"status":"healthy","keys_available":5,"timestamp":"..."}
```

### 6. Update Star Shell
Update the backend URL in `star_shell/main.py`:

```python
backend_url = "https://your-project-name.vercel.app"
```

## 🎯 Advantages over Render:
- **No sleep** - always fast response
- **Global CDN** - fast from anywhere
- **Serverless** - scales automatically
- **Free forever** - no time limits

## 📁 File Structure:
```
backend_service/
├── api/
│   ├── health.py      # Health check endpoint
│   └── generate.py    # Main API endpoint
├── vercel.json        # Vercel configuration
├── requirements.txt   # Python dependencies
└── DEPLOY_VERCEL.md   # This guide
```

## 🔧 How It Works:
- Each Python file in `api/` becomes a serverless function
- `vercel.json` configures routing
- Environment variables store your API keys securely
- Functions run on-demand (no sleep issues)

## 🚨 Important Notes:
- Vercel has generous free limits (100GB bandwidth, 100 serverless function invocations per day)
- Perfect for your secret backend use case
- Much more reliable than services that sleep
- Professional infrastructure used by major companies