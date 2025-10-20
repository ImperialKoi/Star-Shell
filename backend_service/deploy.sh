#!/bin/bash

echo "🚀 Star Shell Vercel Deployment Script"
echo "======================================"

# Check if we're in the right directory
if [ ! -f "vercel.json" ]; then
    echo "❌ Error: Please run this script from the backend_service directory"
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial Star Shell Vercel backend"
else
    echo "📦 Git repository already initialized"
fi

# Check if remote exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo ""
    echo "🔗 Please create a GitHub repository and add the remote:"
    echo "   1. Go to https://github.com and create a new repository"
    echo "   2. Run: git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
    echo "   3. Run: git push -u origin main"
    echo ""
    echo "Then deploy to Vercel:"
    echo "   1. Go to https://vercel.com"
    echo "   2. Sign up with GitHub (no credit card needed)"
    echo "   3. Import your repository"
    echo "   4. Add environment variables (your 5 Gemini API keys)"
    echo "   5. Deploy!"
else
    echo "🔗 Remote origin already configured"
    echo "📤 Pushing to GitHub..."
    git add .
    git commit -m "Update Star Shell backend" || echo "No changes to commit"
    git push
    echo ""
    echo "✅ Pushed to GitHub!"
    echo ""
    echo "🌐 Now deploy to Vercel:"
    echo "   1. Go to https://vercel.com"
    echo "   2. Import your repository"
    echo "   3. Add environment variables"
    echo "   4. Deploy!"
fi

echo "🎉 Happy deploying!"