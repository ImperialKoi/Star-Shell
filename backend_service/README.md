# Star Shell Vercel Backend

Deploy your Star Shell backend to Vercel for free with no credit card required.

## 🚀 Complete Deployment Guide

### Step 1: Prepare Your Repository

1. **Navigate to backend directory**:
   ```bash
   cd backend_service
   ```

2. **Initialize Git repository**:
   ```bash
   git init
   git add .
   git commit -m "Star Shell Vercel backend"
   ```

3. **Create GitHub repository**:
   - Go to [github.com](https://github.com) and create a new repository
   - Name it `star-shell-backend` (or any name you prefer)
   - Don't initialize with README (we already have files)

4. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/star-shell-backend.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Vercel

1. **Go to Vercel**:
   - Visit [vercel.com](https://vercel.com)
   - Click "Sign up" and choose "Continue with GitHub"
   - No credit card required!

2. **Import Project**:
   - Click "New Project"
   - Find your `star-shell-backend` repository
   - Click "Import"

3. **Configure Project**:
   - **Project Name**: `star-shell-backend` (or your choice)
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - Click "Deploy"

### Step 3: Add Environment Variables

1. **Go to Project Settings**:
   - After deployment, go to your project dashboard
   - Click "Settings" tab
   - Click "Environment Variables" in the sidebar

2. **Add Your API Keys**:
   ```
   Variable Name: GEMINI_KEY_1
   Value: your_first_gemini_api_key_here
   
   Variable Name: GEMINI_KEY_2
   Value: your_second_gemini_api_key_here
   
   Variable Name: GEMINI_KEY_3
   Value: your_third_gemini_api_key_here
   
   Variable Name: GEMINI_KEY_4
   Value: your_fourth_gemini_api_key_here
   
   Variable Name: GEMINI_KEY_5
   Value: your_fifth_gemini_api_key_here
   
   Variable Name: STAR_SHELL_SECRET
   Value: secret-3.14159
   ```

3. **Redeploy**:
   - Go to "Deployments" tab
   - Click the three dots on the latest deployment
   - Click "Redeploy"

### Step 4: Test Your Deployment

Your backend will be available at: `https://your-project-name.vercel.app`

Test the health endpoint:
```bash
curl https://your-project-name.vercel.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "keys_available": 5,
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

### Step 5: Update Star Shell

1. **Get your Vercel URL** from the deployment dashboard
2. **Update `star_shell/main.py`**:
   ```python
   backend_url = "https://your-actual-project-name.vercel.app"
   ```

### Step 6: Test the Secret Option

1. **Rebuild and install** your updated Star Shell:
   ```bash
   # In your main project directory
   pip install --upgrade dist/star_shell-0.2.1-py3-none-any.whl
   ```

2. **Test the secret backend**:
   ```bash
   star-shell init
   # When prompted for backend, enter: secret-3.14159
   ```

## 📁 Project Structure

```
backend_service/
├── api/
│   ├── health.py      # Health check endpoint (/health)
│   └── generate.py    # Main API endpoint (/api/generate)
├── vercel.json        # Vercel configuration
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This guide
```

## 🔧 How It Works

- **Serverless Functions**: Each `.py` file in `api/` becomes an endpoint
- **No Sleep**: Functions run on-demand, always responsive
- **Global CDN**: Fast response times worldwide
- **Automatic Scaling**: Handles traffic spikes automatically

## 🎯 Benefits

- ✅ **Free forever** - no credit card required
- ✅ **No sleep issues** - always fast
- ✅ **Professional infrastructure**
- ✅ **Automatic HTTPS**
- ✅ **Global edge network**
- ✅ **Easy updates** via GitHub

## 🚨 Important Notes

- Keep your environment variables secure
- Monitor your Gemini API usage in Google Cloud Console
- Vercel free tier includes 100GB bandwidth and generous function limits
- Perfect for your secret backend use case

## 🔄 Making Updates

To update your backend:
1. Make changes to your code
2. Push to GitHub: `git push`
3. Vercel automatically redeploys!

## 📊 Monitoring

- Check Vercel dashboard for function logs
- Monitor API usage in Google Cloud Console
- Set up billing alerts for your Gemini API keys