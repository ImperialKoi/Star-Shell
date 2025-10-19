# Star Shell Backend Service

This is a secure proxy service that manages your Gemini API keys with automatic rotation and error handling.

## Features

- **Key Rotation**: Automatically rotates between 5 API keys
- **Error Recovery**: Skips failed keys and retries with others
- **Rate Limit Handling**: Intelligent handling of quota limits
- **Secure**: API keys never exposed to end users
- **Monitoring**: Usage statistics and health checks

## Local Development

1. **Set up environment**:
   ```bash
   cd backend_service
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**:
   ```bash
   python app.py
   ```

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI** and login
2. **Create app**:
   ```bash
   heroku create your-star-shell-backend
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set GEMINI_KEY_1=your_first_key
   heroku config:set GEMINI_KEY_2=your_second_key
   heroku config:set GEMINI_KEY_3=your_third_key
   heroku config:set GEMINI_KEY_4=your_fourth_key
   heroku config:set GEMINI_KEY_5=your_fifth_key
   heroku config:set STAR_SHELL_SECRET=secret-3.14159
   ```

4. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   heroku git:remote -a your-star-shell-backend
   git push heroku main
   ```

### Option 2: Railway

1. **Connect your GitHub repo** to Railway
2. **Set environment variables** in Railway dashboard
3. **Deploy automatically** on push

### Option 3: DigitalOcean App Platform

1. **Create new app** from GitHub repo
2. **Set environment variables**
3. **Deploy**

## Security Notes

- API keys are stored as environment variables, never in code
- The secret token (`secret-3.14159`) provides access control
- All requests are logged for monitoring
- Keys are automatically rotated to prevent overuse

## API Endpoints

- `GET /health` - Health check
- `POST /api/generate` - Generate content (requires Bearer token)
- `GET /api/stats` - Usage statistics (requires Bearer token)

## Monitoring

Check your deployment logs to monitor:
- Key rotation patterns
- Error rates
- Usage statistics
- Performance metrics

## Cost Management

- Monitor your Gemini API usage in Google Cloud Console
- Set up billing alerts
- The service automatically distributes load across keys
- Failed keys are temporarily disabled to prevent waste